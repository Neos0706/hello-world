<template>
<el-collapse>
    <el-collapse-item title="">
        <el-card class="box-card">
            <el-form>
                <el-form-item label="应用类型">
                </el-form-item>
                <el-form-item label="场景角色">
                    <el-radio v-model="radio" label="1">备选项</el-radio>
                    <el-radio v-model="radio" label="2">备选项</el-radio>
                    <el-radio v-model="radio" label="2">备选项</el-radio>
                </el-form-item>
                <el-form-item label="包链接|web url">
                </el-form-item>
                <el-form-item label="采集源">
                </el-form-item>               
            </el-form>
        </el-card>
        <el-card class="box-card">
        </el-card>
    </el-collapse-item>    
</el-collapse>
</template>

<script>
export default {
    name:'OneDevSetting',
    props:{
        form:Object
    }
    
}
</script>

<style>

</style>