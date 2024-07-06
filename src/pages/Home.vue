<template>
    <div>
        <el-container>

            <el-aside style="width: 200px; min-height: 100vh; background-color: rgba(0,21,41)">
                <div
                    style="height: 60px; line-height:60px; color: white; display: flex; justify-content:center; align-items: center;">
                    logo
                </div>

                <el-menu router background-color="rgba(27, 38, 58)" text-color="rgba(255, 255, 255, 0.65)"
                    active-text-color="#fff" style="border: none" :default-active="$route.path">
                    <el-menu-item index="/home">
                        <i class="el-icon-s-home"></i>
                        <span slot="title">系统首页</span>
                    </el-menu-item>

                    <el-submenu index="/" v-if="user.role === '学生'"> 
                        <template slot="title">
                            <i class="el-icon-s-order"></i>
                            <span slot="title">信息界面</span>
                        </template>
                        <el-menu-item index="/1">
                            <span slot="title">个人信息</span>
                        </el-menu-item>
                        <el-menu-item index="/2">
                            <span slot="title">比赛报名</span>
                        </el-menu-item>
                        <el-menu-item index="/3">
                            <span slot="title">查看成绩</span>
                        </el-menu-item>
                    </el-submenu>

                    <el-menu-item index="/4" v-if="user.role === '教师'">
                        <i class="el-icon-upload2"></i>
                        <span slot="title">登记成绩</span>
                    </el-menu-item>
                    <el-submenu index="/" v-if="user.role === '教师'"> 
                        <template slot="title">
                            <i class="el-icon-s-order"></i>
                            <span slot="title">查看信息</span>
                        </template>
                        <el-menu-item index="/5">
                            <span slot="title">查看学生</span>
                        </el-menu-item>
                        <el-menu-item index="/6">
                            <span slot="title">查看学院</span>
                        </el-menu-item>
                    </el-submenu>
                    
                    <el-menu-item index="/7" v-if="user.role === '管理员'">
                        <i class="el-icon-circle-plus"></i>
                        <span slot="title">添加比赛</span>
                    </el-menu-item>
                    
                    <el-submenu index="/" v-if="user.role === '管理员'"> 
                        <template slot="title">
                            <i class="el-icon-s-order"></i>
                            <span slot="title">查看信息</span>
                        </template>
                        <el-menu-item index="/8">
                            <span slot="title">学生信息</span>
                        </el-menu-item>
                        <el-menu-item index="/6">
                            <span slot="title">学院信息</span>
                        </el-menu-item>
                    </el-submenu>

                    <el-menu-item index="/tmplate">
                        <i class="el-icon-s-tools"></i>
                        <span slot="title">系统设置</span>
                    </el-menu-item>
                </el-menu>

            </el-aside>
            <el-container>
                <el-header>
                    <el-breadcrumb separator-class="el-icon-arrow-right" style="">
                        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                        <el-breadcrumb-item :to="{ path: '/404' }">管理</el-breadcrumb-item>
                    </el-breadcrumb>
                    <div style="flex: 1; width: 0; display:flex; align-items: center; justify-content: flex-end">
                        <el-dropdown placement="bottom" style="">
                            <div style="display:flex; align-items: center; cursor: default;">
                                <span style="margin-right: 10px;">{{ user.username }}</span>
                                <img src="@/assets/image/Diamond.jpg" alt=""
                                    style="border-radius: 50%; overflow: hidden; width:45px; ">
                            </div>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item>个人信息</el-dropdown-item>
                                <el-dropdown-item>修改密码</el-dropdown-item>
                                <el-dropdown-item @click.native="logout">退出登录</el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                    </div>
                </el-header>

                <el-main>
                    <router-view />
                </el-main>
            </el-container>

        </el-container>
    </div>
</template>

<script>

import request from "@/utils/request";

export default {
    name: 'Home',
    data() {
        return {
            inputstr: '',
            students: [],
            multist: [],
            pages: [],
            pagination: {},
            total: 0,
            pagesize: 10,
            currentpage: 1,
            user: JSON.parse(localStorage.getItem('User') || '{}'),
        }
    },
    mounted() {
    },
    methods: {
        getstudent() {

        },
        logout() {
            localStorage.removeItem('User')
            this.$router.push('/login')
        },
        handleSelectionChange() {
            this.multist = data;
            console.log(data);
        }
    }
}
</script>

<style>
.el-menu--inline {
    background-color: rgba(32, 43, 71) !important;
}

.el-menu--inline .el-menu-item {
    background-color: rgba(32, 43, 71) !important;
    padding-left: 49px !important;
}

.el-menu-item:hover,
.el-submenu__title:hover {
    background-color: rgba(45, 60, 89) !important;
    border-radius: 5px !important;
    color: #fff !important;
    /* */
}

.el-submenu__title:hover i {
    color: #fff !important;
}

.el-menu-item.is-active {
    background-color: rgba(45, 60, 89) !important;
    border-radius: 5px !important;
    margin: 4px !important;
}

.el-menu-item {
    height: 40px !important;
    line-height: 40px !important;
    margin: 4px !important;
}

.el-submenu__title {
    height: 40px !important;
    line-height: 40px !important;
    margin: 4px !important;
}

.el-aside {
    box-shadow: 2px 0 6px rgba(0, 21, 41, 0.35);
}

.el-header {
    box-shadow: 2px 0 6px rgba(0, 21, 41, 0.35);
    display: flex;
    align-items: center;
}
</style>
