<template>
    <!-- box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); -->
    <div>
        <div style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); padding:10px 20px; border-radius: 5px; margin-bottom:10px; width: 97%; text-align: center">欢迎使用kinoki开发的运动会管理系统</div>
        <div
            style=" padding:10px 20px; border-radius: 5px; margin-bottom:10px; height:60%; width:60%; align-items:center; margin-left: 20%;">
            <div class="block">
                <el-carousel height="400px">
                    <el-carousel-item v-for="item in 4" :key="item">
                        <h3 class="small"></h3>
                    </el-carousel-item>
                </el-carousel>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Welcome',
};
</script>

<style scoped>
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
</style>