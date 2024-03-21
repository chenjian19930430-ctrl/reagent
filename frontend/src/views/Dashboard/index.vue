<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Dashboard</h1>
    <div class="grid grid-cols-4 gap-4">
      <div class="stat-card"><h3>活跃线索</h3><p class="text-3xl font-bold text-blue-600">1,280</p></div>
      <div class="stat-card"><h3>今日视频发布</h3><p class="text-3xl font-bold text-green-600">24</p></div>
      <div class="stat-card"><h3>客服会话</h3><p class="text-3xl font-bold text-orange-600">56</p></div>
      <div class="stat-card"><h3>营销活动</h3><p class="text-3xl font-bold text-purple-600">8</p></div>
    </div>
  </div>
</template>
<style scoped>
.stat-card { background:#fff;padding:24px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.06); }
.stat-card h3 { color:#909399;font-size:14px;margin-bottom:8px; }
</style>
