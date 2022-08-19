<template>
  <div>
  <el-menu :default-active="activeIndex" :router=true  class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
    <el-menu-item index="index">首页</el-menu-item>
    <el-submenu index="2">
      <template slot="title">我的工作台</template>
      <el-menu-item index="eldemo">eldemo</el-menu-item>
      <el-menu-item index="wayang">wayang</el-menu-item>
      <el-menu-item index="2-3">选项3</el-menu-item>
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
    </el-submenu>
    <el-menu-item index="3">消息中心</el-menu-item>
    <el-menu-item index="4"><a href="#" target="_blank">订单管理</a></el-menu-item>
  </el-menu>
    <app-main />
  </div>
</template>

<script>
import {AppMain} from './components'
export default {
    name:'Layout',
    data(){
      return {
        activeIndex:"1",
      }
    },
    
    methods: {
      handleSelect(key, keyPath){
        //console.log(`key===>${key},keyPath===>${keyPath}`)
      },
    },
    components:{
      AppMain,
    }
    
}
</script>

<style lang="scss" scoped>

</style>