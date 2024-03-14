<template>
  <div class="dashboard-layout">
    <aside class="sidebar">
      <div class="logo">ReAgent</div>
      <el-menu router :default-active="route.path" background-color="#304156" text-color="#bfcbd9" active-text-color="#409eff">
        <el-menu-item index="/dashboard"><span>Dashboard</span></el-menu-item>
        <el-menu-item index="/videos"><span>短视频</span></el-menu-item>
        <el-menu-item index="/cs"><span>AI客服</span></el-menu-item>
        <el-menu-item index="/leads"><span>线索</span></el-menu-item>
        <el-menu-item index="/marketing"><span>营销</span></el-menu-item>
        <el-menu-item index="/documents"><span>文档</span></el-menu-item>
      </el-menu>
    </aside>
    <main class="main-content">
      <header class="header"><h2>重构智能 ReAgent</h2><el-button @click="logout">退出</el-button></header>
      <div class="content"><router-view /></div>
    </main>
  </div>
</template>
<script setup lang="ts">
import { useRoute,useRouter } from "vue-router"
const route = useRoute();const router = useRouter()
const logout = ()=>{localStorage.removeItem("token");router.push("/login")}
</script>
<style scoped>
.dashboard-layout {display:flex;height:100vh}
.sidebar {width:240px;background:#304156;color:#bfcbd9}
.logo {height:60px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:bold;border-bottom:1px solid rgba(255,255,255,0.1);color:#fff}
.main-content {flex:1;display:flex;flex-direction:column}
.header {height:60px;display:flex;align-items:center;justify-content:space-between;padding:0 24px;background:#fff;border-bottom:1px solid #e4e7ed}
.content {flex:1;overflow-y:auto;background:#f0f2f5}
</style>
