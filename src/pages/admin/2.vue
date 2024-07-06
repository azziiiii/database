<template>
    <div>
        <!-- 表格上端查询 -->
        <el-card>
            <el-form :inline="true" style="margin-top: 20px; margin-left: 0px;">
                <el-row>
                    <el-col :span="10">
                        <el-form-item label="请输入查询条件：">
                            <el-input v-model="inputstr" placeholder="请输入查询条件" style="width: 350px;"></el-input>
                        </el-form-item>
                    </el-col>

                    <el-col :span="14">
                        <el-button-group>
                            <el-button type="primary" icon="el-icon-zoom-in" @click="getstudent">查询</el-button>
                            <el-button type="primary" icon="el-icon-folder" @click="">全部</el-button>
                            <el-button type="primary" icon="el-icon-circle-plus-outline" @click="">添加</el-button>
                        </el-button-group>
                    </el-col>
                </el-row>
            </el-form>
            <!-- 表格 -->
            <div>
                <el-table :data="pages" border style="width: 100%"
                    @selection-change="handleSelectionChange">
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column type="index" label="序号" align="center" width="80">
                    </el-table-column>
                    <el-table-column label="学号" prop="id" align="center" width="215"></el-table-column>
                    <el-table-column label="姓名" prop="name" align="center" width="215"></el-table-column>
                    <el-table-column label="性别" prop="gender" align="center" width="215"></el-table-column>
                    <el-table-column label="年级" prop="grade" align="center" width="215"></el-table-column>
                    <el-table-column label="项目" prop="event" align="center" width="215"></el-table-column>
                    <el-table-column label="奖项" prop="award" align="center" width="214"></el-table-column>
                </el-table>
                <el-row style="margin-top: 20px;">
                    <el-col :span="8" style="text-align: left">
                        <el-button type="danger" icon="el-icon-delete" size="mini"
                            @click="deletestudents">批量删除</el-button>
                    </el-col>
                    <el-col :span="16" style="text-align: right;">
                        <el-pagination :current-page="currentpage" :page-sizes="[5, 10, 50, 100]" :page-size="pagesize"
                            layout="total, sizes, prev, pager, next, jumper" :total="total"
                            @size-change="handleSizeChange" @current-change="handleCurrentChange">
                        </el-pagination>
                    </el-col>
                </el-row>
            </div>
        </el-card>
    </div>
</template>

<script>
import request from "@/utils/request";
export default {
    name: "admin2",
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
        request.get('/function1/').then(res => {
            this.pages = res.data;
            this.total = res.data.length;
        })
    },
    methods: {}
}
</script>

<style scoped></style>