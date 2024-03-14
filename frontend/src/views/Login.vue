<template>
  <div class="login-container">
    <div class="login-card">
      <h1 class="text-2xl font-bold text-center mb-6">ReAgent 重构智能</h1>
      <el-form :model="form" label-width="80px">
        <el-form-item label="用户名"><el-input v-model="form.username" /></el-form-item>
        <el-form-item label="密码"><el-input v-model="form.password" type="password" /></el-form-item>
        <el-form-item><el-button type="primary" @click="handleLogin" class="w-full">登录</el-button></el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue"
import { useRouter } from "vue-router"
import { login } from "../api/auth"
const router = useRouter()
const form = ref({username:"",password:""})
const handleLogin = async () => {
  try { const res = await login(form.value); localStorage.setItem("token",res.data.access_token); router.push("/") }
  catch(e) { console.error(e) }
}
</script>
<style scoped>
.login-container { display:flex;justify-content:center;align-items:center;height:100vh;background:#f0f2f5; }
.login-card { width:400px;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 12px rgba(0,0,0,0.1); }
</style>
