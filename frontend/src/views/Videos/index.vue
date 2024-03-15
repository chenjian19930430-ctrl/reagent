<template>
  <div class="p-6">
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">短视频管理</h1>
      <el-button type="primary">新建视频</el-button>
    </div>
    <el-table :data="videos" stripe>
      <el-table-column prop="title" label="标题" />
      <el-table-column prop="status" label="状态"><template #default="{row}"><el-tag :type="row.status=='published'?'success':'warning'">{{row.status}}</el-tag></template></el-table-column>
      <el-table-column prop="platforms" label="平台" />
      <el-table-column prop="views" label="播放量" />
      <el-table-column prop="likes" label="点赞" />
    </el-table>
  </div>
</template>
<script setup lang="ts">
import { ref,onMounted } from "vue"
import { getVideos } from "../../api/videos"
const videos = ref([])
onMounted(async()=>{const res=await getVideos();videos.value=res.data})
</script>
