<template>
    <div
    style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">
        <el-table :data="table" border style="width: 100%">
            <el-table-column prop="event_id" label="比赛编号" width="283" align="center">
            </el-table-column>
            <el-table-column prop="event_name" label="比赛项目" width="283" align="center">
            </el-table-column>
            <el-table-column prop="score" label="比赛成绩" width="283" align="center">
            </el-table-column>
            <el-table-column prop="point" label="比赛积分" width="283" align="center">
            </el-table-column>
            <el-table-column prop="rank" label="比赛名次" width="283" align="center">
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
    name: "teacher4",
    data() {
        return {
            user: JSON.parse(localStorage.getItem('User') || '{}'),
            table: [],
            currentpage: 1,
            pagesize: 10,
            total: 0,
        }
    },
    mounted() {
        this.getpages()
    },
    methods: {
        getpages()
        {
            request .post('/function6/', {sno : this.user.username, num: this.currentpage, size : this.pagesize}).then(res => {
                console.log(res.data)
                this.table = res.data
                this.total = res.pagination.total_items
                this.$message({ message: '数据加载成功!', type: 'success' })
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
    }
}
</script>

<style scoped></style>