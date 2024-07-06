<template>
    <div
        style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">
        <el-form :inline="true" style="margin-top: 20px; margin-left: 0px;">
            <el-row>
                <el-col :span="8">
                    <el-form-item label="查询：">
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
            <el-table-column prop="athlete_id" label="学号" width="180" align="center">
            </el-table-column>
            <el-table-column prop="athlete_name" label="姓名" width="180" align="center">
            </el-table-column>
            <el-table-column prop="event_id" label="比赛编号" width="180" align="center">
            </el-table-column>
            <el-table-column prop="event_name" label="比赛项目" width="180" align="center">
            </el-table-column>
            <el-table-column prop="score" label="比赛成绩" width="180" align="center">
            </el-table-column>
            <el-table-column prop="point" label="比赛积分" width="180" align="center">
            </el-table-column>
            <el-table-column prop="rank" label="比赛名次" width="180" align="center">
            </el-table-column>
            <el-table-column label="登记比赛" align="center">
                <template slot-scope="scope">
                    <el-button type="success" icon="el-icon-edit" size="mini" @click="dengji(scope.row)">登记</el-button>
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

        <el-dialog :title="dengjibiao" :visible.sync="dialogVisible" width="30%" :close-on-click-modal="false"
            @close="closeform('form')">
            <el-form :model="form" :rules="rules" ref="form" :inline="true" size="mini" label-width="110px"
                label-position="right" style="margin-left: -50px;">
                <el-form-item label="姓名" prop="athlete_name">
                    <el-input suffix-icon="el-icon-edit" v-model="form.athlete_name" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="学号" prop="athlete_id">
                    <el-input suffix-icon="el-icon-edit" v-model="form.athlete_id" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="比赛项目" prop="event_name">
                    <el-input suffix-icon="el-icon-edit" v-model="form.event_name" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="比赛成绩" prop="score">
                    <el-select placeholder="请选择比赛成绩" v-model="form.score">
                        <el-option label="特等奖" value="特等奖"></el-option>
                        <el-option label="一等奖" value="一等奖"></el-option>
                        <el-option label="二等奖" value="二等奖"></el-option>
                        <el-option label="三等奖" value="三等奖"></el-option>
                        <el-option label="参与奖" value="参与奖"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="比赛积分" prop="point">
                    <el-input suffix-icon="el-icon-edit" v-model="form.point"></el-input>
                </el-form-item>
                <el-form-item label="比赛名次" prop="rank">
                    <el-input suffix-icon="el-icon-edit" v-model="form.rank"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" size="mini" @click="submitform('form')">确
                    定</el-button>
                <el-button type="info" size="mini" @click="closeform('form')">取 消</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import request from '@/utils/request';

export default {
    name: "athlete3",
    data() {
        return {
            user: JSON.parse(localStorage.getItem('User') || '{}'),
            currentpage: 1,
            askfl: false,
            pagesize: 10,
            inputstr: '',
            total: 1,
            table: [],
            dialogVisible: false,
            dengjibiao: '',
            form: {
                athlete_id: '',
                athlete_name: '',
                event_id: '',
                event_name: '',
                score: '',
                point: '',
                rank: '',
            },
            rules: {
                score: [{ required: true, message: '请输入成绩', trigger: 'blur' },],
                point: [{ required: true, message: '请输入该学生的积分', trigger: 'blur' }, { pattern: /^[0-9]+$/, message: '格式错误', trigger: 'blur' },],
                rank: [{ required: true, message: '请输入该学生的排名', trigger: 'blur' }, { pattern: /^[0-9]+$/, message: '格式错误', trigger: 'blur' },],
            },
        }
    },
    mounted() {
        this.getpages();
    },
    methods: {
        dengji(row) {
            this.dengjibiao = "登记表"
            this.dialogVisible = true
            this.form = JSON.parse(JSON.stringify(row))
        },
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
            request.post('/function7/', { sno: this.user.username, size: this.pagesize, num: this.currentpage }).then(res => {
                this.table = res.data
                this.total = res.pagination.total_items
                this.$message({ message: '数据加载成功!', type: 'success' })
            })
        },
        ask() {
            this.table = []
            this.askfl = true
            request.post('/function8/', { input: this.inputstr, size: this.pagesize, num: this.currentpage }).then(res => {
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
        closeform(formName) {
            this.$refs[formName].resetFields();
            this.dialogVisible = false;
            this.form.athlete_id = '';
            this.form.athlete_name = '';
            this.form.event_id = '';
            this.form.event_name = '';
            this.form.score = '';
            this.form.point = '';
            this.form.rank = '';
        },
        submitform(formName) {
            console.log(this.form)
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    this.submitDB();
                }
                else {
                    console.log('error submit!!!');
                    return false;
                }
            })
        },
        submitDB() {
            let _this = this
            this.$confirm('是否登记该学生比赛信息?',
                {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    request.post('/function9/', { student: this.form })
                        .then(res => {
                            console.log(res.code)
                            if(res.code == 200)
                            {
                                _this.getpages();
                                _this.$message({
                                    message: '登记成功!',
                                    type: 'success'
                                });
                            }
                        })
                }).catch(() => {
                    _this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
        },
    }
}
</script>

<style scoped></style>