<template>
    <div id="login"
        style="height:100vh; display:flex; align-items: center; justify-content: center; background-color: #0f9876;">
        <div
            style="background-color: rgba(255, 255, 255, 0.8); display:flex; padding: 20px; border-radius: 8px; width:30%;; overflow:hidden">
            <div style="flex: 1; display: flex; align-items:center; justify-content: center;">
                <el-form :model="user" style="width:80%" :rules="rules" ref="loginref">
                    <div style="text-align: center; font-size: 24px; font-weight: bold; margin-bottom: 30px; margin-top: 30px">欢迎登录后台管理系统
                    </div>
                    <el-form-item prop="username" style="margin: 30px auto; width: 70%;">
                        <el-input prefix-icon="el-icon-user" placeholder="请输入账号" v-model="user.username"></el-input>
                    </el-form-item>
                    <el-form-item prop="password" style="margin: 30px auto; width: 70%;">
                        <el-input prefix-icon="el-icon-lock" show-password placeholder="请输入密码" v-model="user.password"></el-input>
                    </el-form-item>
                    <el-form-item prop="code" style="margin: 30px auto; width: 70%;">
                        <div style="display: flex; ">
                            <el-input prefix-icon="el-icon-circle-check" placeholder="请输入验证码" style="flex: 1" v-model="user.code"></el-input>
                            <div style="flex: 1; height: 40px;">
                                <ValidCode @update:value="getCode"/>
                            </div>
                        </div>
                    </el-form-item>
                    <el-form-item>
                        <el-button class="custom-button" type="primary"
                            style="margin: 0 15%; width: 70%;" @click="login">登录</el-button>
                    </el-form-item>
                    <div style="display: flex; margin: 25px 15%; width: 70%; font-size: 14px;">
                    <div style="flex: 1">还没有账号? 请 <span style="color: #0f9876; cursor: pointer; " @click="$router.push('/register')">注册</span></div>
                    <div style="flex: 1; text-align: right;"><span style="color: #0f9876; cursor: pointer;">忘记密码</span></div>
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
    name:'Login',
    components:{
        ValidCode
    },
    data(){

        const validatecode = (rule, value, callback) => {
            if (value === '') {
            callback(new Error('请输入验证码'))
            } else {
            if (value.toLowerCase() !== this.code) {
                callback(new Error('验证码错误'))
            }
            else callback()
            }
        }

        return {
            code: '',
            user: {
                username: '',
                password: '',
                role: '学生',
                code: '',
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
                code: 
                [
                    { validator: validatecode, trigger: 'blur' }
                ],
            }
        }
    },
    created(){
        // request.getCode
    },
    methods:{
        getCode(code)
        {
            this.code = code.toLowerCase();
        },
        login()
        {
            this.$refs['loginref'].validate((valid) => {
              if (valid) {
                  this.$request.post('/login/', this.user).then(res=>
                    {
                        if(res.code === '200')
                        {
                            this.$router.push('/')
                            this.$message.success('登陆成功')
                            localStorage.setItem("User", JSON.stringify(res.data))
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