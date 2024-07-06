<template>
    <div id="login"
        style="height:100vh; display:flex; align-items: center; justify-content: center; background-color: #2596be;">
        <div
            style="background-color: rgba(255, 255, 255, 0.8); display:flex; padding: 20px; border-radius: 8px; width:30%; overflow:hidden">
            <div style="flex: 1; display: flex; align-items:center; justify-content: center;">
                <el-form :model="user" style="width:80%;" :rules="rules" ref="registeref">
                    <div style="text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 30px; margin-top: 30px">欢迎注册后台管理系统
                    </div>
                    <el-form-item prop="username" style="margin: 30px auto; width: 70%;">
                        <el-input prefix-icon="el-icon-user" placeholder="请输入账号" v-model="user.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password" style="margin: 30px auto; width: 70%;">
                        <el-input prefix-icon="el-icon-lock" show-password placeholder="请输入密码" v-model="user.password"></el-input>
                    </el-form-item>
                    <el-form-item prop="confirmpwd" style="margin: 30px auto; width: 70%;">
                        <el-input prefix-icon="el-icon-lock" show-password placeholder="请确认密码" v-model="user.confirmpwd"></el-input>
                    </el-form-item>
                    <el-form-item prop="confirmpwd" style="margin: 5px auto; width: 70%; transform: translateY(-20px);">
                       <el-radio-group v-model="user.role">
                            <el-radio label="学生"></el-radio>
                            <el-radio label="教师"></el-radio>
                       </el-radio-group>
                    </el-form-item>
                    <el-form-item>
                        <el-button class="custom-button" type="danger"
                            style="margin: 0 15%; width: 70%; transform: translateY(-20px);" @click="register">注册</el-button>
                    </el-form-item>
                    <div style="display: flex; margin: 15px 15%; width: 70%; font-size: 14px; transform: translateY(-20px);">
                    <div style="flex: 1">已有账号? 请 <span style="color: #46b7d5; cursor: pointer; " @click="$router.push('/login')">登录</span></div>
                    <div style="flex: 1; text-align: right;"><span style="color: #46b7d5; cursor: pointer;" @click="$router.push('/login')">返回</span></div>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
import ValidCode from '@/components/ValidCode';
import request from '@/utils/request'

export default {
    name:'Register',
    data(){

        const validatepwd = (rule, confirmpwd, callback) => {
            if (confirmpwd === '') {
            callback(new Error('请确定密码'))
            } else {
            if (confirmpwd !== this.user.password) {
                callback(new Error('两次输入密码不一致'))
            }
            else callback()
            }
        }

        return {
            user: {
                username: '',
                password: '',
                confirmpwd: '',
                role: '',
            },
            rules: {
                username: 
                [
                    { required: true, message: '请输入账号', trigger: 'blur' },
                ],
                password:
                [
                    { required: true, message: '请输入密码', trigger: 'blur' },
                ],
                confirmpwd: 
                [
                    { validator: validatepwd, trigger: 'blur' },
                ],
                role: 
                [
                    { required: true, message:'请选择', trigger: 'blur' },
                ],
            }
        }
    },
    created(){

    },
    methods:{
        getCode(code)
        {
            this.code = code.toLowerCase();
        },
        register()
        {
            this.$refs['registeref'].validate((valid) => {
              if (valid) {
                  this.$request.post('/register/', this.user).then(res=>
                    {
                        if(res.code === '200')
                        {
                            this.$router.push('/login')
                            this.$message.success('注册成功')
                            // localStorage.setItem("User", JSON.stringify(res.data))
                        }
                        else 
                        {
                            this.$message.error(res.msg)
                        }
                    })
              }
            });
        },
    }
}
</script>