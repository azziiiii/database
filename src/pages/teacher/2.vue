<template>
    <div
        style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">
        <el-form :inline="true" style="margin-top: 20px; margin-left: 0px;">
            <el-row>
                <el-col :span="8">
                    <el-form-item label="查询学生:">
                        <el-input v-model="inputstr" placeholder="请输入" style="width: 350px;"></el-input>
                    </el-form-item>
                </el-col>

                <el-col :span="3">
                    <el-button-group>
                        <el-button type="primary" icon="el-icon-search" @click="ask">搜索</el-button>
                        <el-button type="primary" icon="el-icon-folder" @click="all">全部</el-button>
                    </el-button-group>
                </el-col>
                <el-col :span="13">
                </el-col>
            </el-row>
        </el-form>
        <el-table :data="table" border style="width: 100%">
            <el-table-column prop="athlete__id" label="学号" width="177" align="center">
            </el-table-column>
            <el-table-column prop="athlete__name" label="姓名" width="177" align="center">
            </el-table-column>
            <el-table-column prop="athlete__gender" label="性别" width="177" align="center">
            </el-table-column>
            <el-table-column prop="athlete__grade" label="年级" width="177" align="center">
            </el-table-column>
            <el-table-column prop="event__name" label="比赛项目" width="177" align="center">
            </el-table-column>
            <el-table-column prop="score" label="比赛成绩" width="177" align="center">
            </el-table-column>
            <el-table-column prop="point" label="比赛积分" width="177" align="center">
            </el-table-column>
            <el-table-column prop="rank" label="比赛名次" width="176" align="center">
            </el-table-column>
        </el-table>
        <el-row style="margin-top: 20px;">
            <el-col :span="24" style="text-align: right;">
                <el-pagination :current-page="currentpage" :page-sizes="[5, 10, 50, 100]" :page-size="pagesize"
                    layout="total, sizes, prev, pager, next, jumper" :total="total" @size-change="handleSizeChange"
                    @current-change="handleCurrentChange">
                </el-pagination>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import request from '@/utils/request';

export default {
    name: "teacher2",
    data() {
        return {
            user: JSON.parse(localStorage.getItem('User') || '{}'),
            currentpage: 1,
            askfl: false,
            pagesize: 10,
            inputstr: '',
            total: 1,
            table: [],
        }
    },
    mounted() {
        this.getpages()
    },
    methods: {
        getpages() {
            request.post('/function10/', { size: this.pagesize, num: this.currentpage }).then(res => {
                console.log(res.data.data)
                this.table = res.data.data
                this.total = res.data.total_records
                this.$message({ message: '加载成功!', type: 'success' })
            })
        },
        handleCurrentChange(num) {
            this.currentpage = num;
            this.getpages()
        },
        handleSizeChange(size) {
            this.pagesize = size;
            this.getpages()
        },
        ask() {
            // this.table = []
            this.askfl = true
            request.post('/function11/', { input: this.inputstr, size: this.pagesize, num: this.currentpage }).then(res => {
                this.table = res.data.data
                this.total = res.data.total_records
                this.$message({ message: '查询成功!', type: 'success' })
            })
        },
        all() {
            this.table = []
            this.askfl = false
            this.inputstr = ""
            this.getpages()
        },
    }
}
</script>

<style scoped></style>