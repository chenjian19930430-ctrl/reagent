<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">文档管理</h1>
    <el-table :data="docs" stripe>
      <el-table-column prop="title" label="标题" />
      <el-table-column prop="doc_type" label="类型" />
      <el-table-column prop="status" label="状态" />
      <el-table-column prop="word_count" label="字数" />
      <el-table-column prop="created_at" label="创建时间" />
    </el-table>
  </div>
</template>
<script setup lang="ts">
import { ref,onMounted } from "vue"
import api from "../../api/index"
const docs = ref([])
onMounted(async()=>{const res=await api.get("/documents");docs.value=res.data})
</script>
