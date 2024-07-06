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
            <el-table-column prop="id" label="比赛编号" width="292" align="center">
            </el-table-column>
            <el-table-column prop="event" label="比赛项目" width="292" align="center">
            </el-table-column>
            <el-table-column prop="score" label="比赛成绩" width="292" align="center">
            </el-table-column>
            <el-table-column prop="point" label="比赛积分" width="292" align="center">
            </el-table-column>
            <el-table-column prop="rank" label="比赛名次" width="291" align="center">
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
            table1: [],
        }
    },
    mounted() {
        // request.get('/function6/').then(res => {
        //     this.pages = res.data;
        //     this.$message({ message: '数据加载成功!', type: 'success' })
        // })
    },
    methods: {
        getpages()
        {

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
            this.table = []
            this.askfl = true
            request.post('/function10/', { input: this.inputstr, size: this.pagesize, num: this.currentpage }).then(res => {
                console.log(res.data)
                this.table = res.data
                this.total = res.total_items
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