<template>
    <div
        style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">
        <el-form :inline="true" style="margin-top: 20px; margin-left: 0px;">
            <el-row>
                <el-col :span="8">
                    <el-form-item label="查询比赛:">
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
        <el-table :data="table1" border style="width: 100%">
            <el-table-column prop="id" label="比赛编号" align="center" width="270">
            </el-table-column>
            <el-table-column prop="name" label="比赛名称" align="center" width="270">
            </el-table-column>
            <el-table-column prop="time" label="比赛时间" align="center" width="270">
            </el-table-column>
            <el-table-column prop="location" label="比赛地点" align="center" width="270">
            </el-table-column>
            <el-table-column label="报名比赛" align="center">
                <template slot-scope="scope">
                    <el-button type="success" icon="el-icon-edit" size="mini" @click="baoming(scope.row)">报名</el-button>
                </template>
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
    name: "athlete2",
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
        this.getpages();
    },
    methods: {
        handleCurrentChange(num) {
            this.currentpage = num;
            if (!askfl) this.getpages()
            else this.ask()
        },
        handleSizeChange(size) {
            this.pagesize = size;
            if (!askfl) this.getpages()
            else this.ask()
        },
        getpages() {
            request.post('/function3/', { sno: this.user.username, size: this.pagesize, num: this.currentpage }).then(res => {
                this.table1 = res.data
                this.total = res.pagination.total_items
                this.$message({ message: '数据加载成功!', type: 'success' })
            })
        },
        ask() {
            this.table1 = []
            this.askfl = true
            request.post('/function4/', { input: this.inputstr, size: this.pagesize, num: this.currentpage }).then(res => {
                console.log(res.data)
                this.table1 = res.data
                this.total = res.total_items
                this.$message({ message: '查询成功!', type: 'success' })
            })
        },
        all() {
            this.table1 = []
            this.askfl = false
            this.inputstr = ""
            this.getpages()
        },
        baoming(row) {
            console.log(this.user.username)
            this.$confirm('确定报名次项目?', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(()=>{
                request .post('/function5/', {sno : this.user.username, id : row.id}).then(res=>{
                    console.log(res)
                    this.$message({
                        message: '报名成功',
                        type: 'success'
                    })
                    this.getpages();
                })
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                })
            })}
    }
}
</script>

<style scoped></style>