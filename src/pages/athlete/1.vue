<template>
    <div style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">
        <el-table :data="pages" border style="width: 100%">
            <el-table-column prop="sno" label="学号" width="235" align="center">
            </el-table-column>
            <el-table-column prop="sname" label="姓名" width="235" align="center">
            </el-table-column>
            <el-table-column prop="cname" label="学院" width="235" align="center">
            </el-table-column>
            <el-table-column prop="coach" label="学院领队" width="235" align="center">
            </el-table-column>
            <el-table-column prop="total_points" label="学院总积分" width="235" align="center">
            </el-table-column>
            <el-table-column prop="rank" label="学院总排名" width="235" align="center">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>

import request from '@/utils/request';

export default {
    name: "athlete1",
    data() {
        return {
            user: JSON.parse(localStorage.getItem('User') || '{}'),
            pages:[],
        }
    },
    mounted() {
        request .post('/function2/', {name: this.user.username}).then(res=>{
            this.pages = res.data
            this.$message({message: '数据加载成功!', type: 'success'})
        })
        // console(user.username)
    },
    methods: {}
}
</script>

<style scoped></style>