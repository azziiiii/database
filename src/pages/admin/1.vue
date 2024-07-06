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

                <el-col :span="5">
                    <el-button-group>
                        <el-button type="primary" icon="el-icon-search" @click="ask">搜索</el-button>
                        <el-button type="primary" icon="el-icon-folder" @click="all">全部</el-button>
                        <el-button type="primary" icon="el-icon-circle-plus-outline" @click="add">添加</el-button>
                    </el-button-group>
                </el-col>
                <el-col :span="13">
                </el-col>
            </el-row>
        </el-form>
        <el-table :data="table" border style="width: 100%">
            <el-table-column type="selection"></el-table-column>
            <el-table-column type="index" label="序号" align="center" width="80">
            </el-table-column>
            <el-table-column prop="event_id" label="比赛编号" width="280" align="center">
            </el-table-column>
            <el-table-column prop="event_name" label="比赛项目" width="280" align="center">
            </el-table-column>
            <el-table-column prop="event_time" label="比赛时间" width="280" align="center">
            </el-table-column>
            <el-table-column prop="event_location" label="比赛地点" width="280" align="center">
            </el-table-column>
            <el-table-column label="操作" align="center">
                <template slot-scope="scope">
                    <el-button type="success" icon="el-icon-more" size="mini" circle
                        @click="view(scope.row)"></el-button>
                    <el-button type="primary" icon="el-icon-edit" size="mini" circle
                        @click="update(scope.row)"></el-button>
                    <el-button type="danger" icon="el-icon-delete" size="mini" circle
                        @click="del(scope.row)"></el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-row style="margin-top: 20px;">
            <el-col :span="8" style="text-align: left">
                <el-button type="danger" icon="el-icon-delete" size="mini" @click="deletestudents">批量删除</el-button>
              </el-col>
            <el-col :span="16" style="text-align: right;">
                <el-pagination :current-page="currentpage" :page-sizes="[5, 10, 50, 100]" :page-size="pagesize"
                    layout="total, sizes, prev, pager, next, jumper" :total="total" @size-change="handleSizeChange"
                    @current-change="handleCurrentChange">
                </el-pagination>
            </el-col>
        </el-row>
        <el-dialog :title="biao" :visible.sync="dialogVisible" width="30%" :close-on-click-modal="false"
            @close="closeform('form')">
            <el-form :model="form" :rules="rules" ref="form" :inline="true" size="mini" label-width="110px"
                label-position="right" style="margin-left: -50px;">
                <el-form-item label="比赛编号" prop="event_id">
                    <el-input suffix-icon="el-icon-edit" v-model="form.event_id" :disabled="isview || isedit"></el-input>
                </el-form-item>

                <el-form-item label="比赛名称" prop="event_name">
                    <el-input suffix-icon="el-icon-edit" v-model="form.event_name"
                        :disabled="isview || isedit"></el-input>
                </el-form-item>

                <el-form-item label="比赛时间" prop="event_time">
                    <el-input suffix-icon="el-icon-edit" v-model="form.event_time" :disabled="isview"></el-input>
                </el-form-item>

                <el-form-item label="比赛地点" prop="event_location">
                    <el-input suffix-icon="el-icon-edit" v-model="form.event_location" :disabled="isview"></el-input>
                </el-form-item>

            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button type="primary" size="mini" v-show="!isview" @click="submit('form')">确
                    定</el-button>
                <el-button type="info" size="mini" @click="closeform('form')">取 消</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import request from '@/utils/request';

export default {
    name: "admin1",
    data() {
        const checkid = (rule, value, callback) => {
            if (this.isedit || this.isadd) {
                callback();
            }
            request.post('/function16/', { id: value }).then((ans) => {
                if (ans.code == 201) {
                    callback(new Error('比赛已存在!'))
                }
                else if (ans.code == 200) {
                    callback()
                }
                else {
                    callback(new Error('服务器异常'));
                }
            }).catch((err) => { console.log(err) })
        }
        const checkname = (rule, value, callback) => {
            if (this.isedit || this.isadd) {
                callback();
            }
            request.post('/function17/', { name: value }).then((ans) => {
                if (ans.code == 201) {
                    callback(new Error('比赛已存在!'))
                }
                else if (ans.code == 200) {
                    callback()
                }
                else {
                    callback(new Error('服务器异常'));
                }
            }).catch((err) => { console.log(err) })
        }
        return {
            user: JSON.parse(localStorage.getItem('User') || '{}'),
            currentpage: 1,
            pagesize: 10,
            inputstr: '',
            total: 1,
            table: [],
            dialogVisible: false,
            biao: '',
            isview: false,
            isadd: false,
            isedit: false,
            form: {
                event_id: '',
                event_name: '',
                event_time: '',
                event_location: '',
            },
            rules: {
                event_id: [
                    { required: true, message: '请输入编号', trigger: 'blur' },
                    { pattern: /^[0-9]+$/, message: '格式错误', trigger: 'blur' },
                    { validator: checkid, trigger: 'blur' },
                ],
                event_name: [
                    { required: true, message: '请输入名称', trigger: 'blur' },
                    { validator: checkname, trigger: 'blur' },
                ],
                event_time: [
                    { required: true, message: '请输入日期', trigger: 'blur' },
                    { pattern: /^(0?[1-9]|1[0-2])\.(0?[1-9]|[12][0-9]|3[01])$/, message: '格式错误', trigger: 'blur' },
                ],
                event_location: [
                    { required: true, message: '请输入地点', trigger: 'blur' },
                ],
            },
        }
    },
    mounted() {
        this.getpages()
    },
    methods: {
        view(row) {
            this.biao = '查看比赛信息'
            this.dialogVisible = true
            this.isview = true
            this.form = JSON.parse(JSON.stringify(row))
        },
        getpages() {
            this.table = []
            request.post('/function14/', { size: this.pagesize, num: this.currentpage }).then(res => {
                console.log(res.data)
                this.table = res.data.data
                this.total = res.data.total
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
            this.table = []
            request.post('/function15/', { input: this.inputstr, size: this.pagesize, num: this.currentpage }).then(res => {
                console.log(res.data)
                this.table = res.data.data
                this.total = res.data.total
                this.$message({ message: '查询成功!', type: 'success' })
            })
        },
        all() {
            this.table = []
            this.inputstr = ""
            this.getpages()
        },
        add() {
            this.dialogVisible = true
            this.isadd = true
            this.biao = '添加比赛项目'
        },
        closeform(formName) {
            this.$refs[formName].resetFields()
            this.form.event_id = ''
            this.form.event_name = ''
            this.form.event_time = ''
            this.form.event_location = ''
            this.dialogVisible = false
            this.isview = false, this.isedit = false, this.isadd = false
        },
        update(row) {
            this.dialogVisible = true;
            this.biao = '修改比赛'
            this.isedit = true
            this.form = JSON.parse(JSON.stringify(row))
        },
        submit(formName) {
            this.$refs[formName].validate((valid) => {
                console.log(valid)
                console.log(this.isadd)
                console.log(this.isedit)
                if (valid) {
                    if (this.isedit) {
                        this.modifyDB();
                    }
                    else if (this.isadd) {
                        this.submitDB();
                    }
                }
                else {
                    console.log('error submit!!!');
                    return false;
                }
            })
        },
        submitDB() {
            let that = this;
            console.log(that.form)
            request.post('/function18/', { form: that.form }).then((ans) => {
                if (ans.code == 200) {
                    that.getpages()
                    that.$message({
                        message: '添加比赛成功!',
                        type: 'success'
                    })
                    that.closeform('form')
                }
                else {
                    that.$message.error('错误')
                }
            }).catch(err => {
                console.log(err);
                that.$message.error('错误')
            })
        },
        modifyDB() {
            let that = this;
            console.log(that.form)
            request.post('/function19/', { form: that.form }).then(ans => {
                if (ans.code == 200) {
                    that.getpages()
                    that.$message({
                        message: '修改比赛成功!',
                        type: 'success'
                    })
                    that.closeform('form')
                }
                else {
                    that.$message.error('错误')
                }
            }).catch(err => {
                console.log(err);
                that.$message.error('错误')
            })
        },
        del(row) {
            let _this = this;
            console.log(row.event_id)
            _this.$confirm('是否删除该比赛?',
                {
                    confirmButtonText: '删除',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    let _this = this;
                    request.post('/function20/', { id: row.event_id })
                        .then(ans => {
                            if (ans.code == 200) {
                                _this.getpages()
                                _this.$message({
                                    message: '删除成功!',
                                    type: 'success'
                                });
                            }
                            else if (ans.code == 402)
                            {
                                _this.$message.error('已经有同学报名过该项目,请先通知学生取消报名')
                            }
                        })
                })
                .catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
        }
    }
}
</script>

<style scoped></style>