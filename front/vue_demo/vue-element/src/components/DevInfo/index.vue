<template>
    <el-descriptions class="margin-top" title="设备状态" :column="4" size="medium" border>
        <!-- <template slot="extra">
        <el-button type="primary" size="small">操作</el-button>
        </template> -->
        <el-descriptions-item v-for="dev in devList" :key="dev.name">
        <template slot="label">
            {{dev.name}}
        </template>
        <el-tag size="small" type="success" v-if="!dev.on">free</el-tag>
        <!-- <el-tag size="small" type="success" >free</el-tag> -->
        <el-tag size="small" type="error" v-else>running</el-tag>
        </el-descriptions-item>
    </el-descriptions> 
</template>

<script>
export default {
    name:'DevInfo',
    props:{
        devList:Array
    }

}
</script>

<style>

</style>