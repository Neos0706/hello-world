<template>
   <el-descriptions class="margin-top" title="配置信息" :column="4" size="medium" border>
        <el-descriptions-item >
            <template slot="label">
                上行设备(发送端)
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                录屏设备
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                弱网设置
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                录屏时长(秒)
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                下行设备(接收端)
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                视频参数
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                测评指标
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
        <el-descriptions-item >
            <template slot="label">
                通知邮箱
            </template>
            <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        </el-descriptions-item>
    </el-descriptions> 
</template>

<script>
export default {

}
</script>

<style>

</style>