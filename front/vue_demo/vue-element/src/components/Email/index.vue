<template>
  <el-form-item :label="'邮箱'+index" >
    <el-input placeholder="请输入内容" v-model="emailObj.email">
        <template slot="append">@agora.io</template>
    </el-input>
    <el-button @click="delEmail(index)">删除</el-button>
  </el-form-item>
</template>

<script>
export default {
    name:'',
    props:{
        index:Number,
        emailObj:Object,
        deleteEmail:Function
    },

    methods:{
        delEmail(index){
            this.deleteEmail(index)
        }
    }
}
</script>

<style>

</style>