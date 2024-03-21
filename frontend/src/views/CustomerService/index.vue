<template>
  <div class="p-6 flex h-full">
    <div class="w-80 border-r pr-4">
      <h2 class="text-lg font-bold mb-4">会话列表</h2>
      <div v-for="s in sessions" :key="s.session_id" class="p-3 mb-2 rounded cursor-pointer hover:bg-gray-100" @click="selectSession(s)">
        <div class="font-medium">{{s.user_name}}</div>
        <div class="text-sm text-gray-500 truncate">{{s.last_message}}</div>
      </div>
    </div>
    <div class="flex-1 pl-4 flex flex-col">
      <h2 class="text-lg font-bold mb-4">AI 客服对话</h2>
      <div class="flex-1 overflow-y-auto mb-4 p-4 bg-gray-50 rounded">
        <div v-for="m in messages" :key="m.id" :class="m.role=='user'?'text-right':''" class="mb-3">
          <div :class="m.role=='user'?'bg-blue-500 text-white':'bg-white'" class="inline-block px-4 py-2 rounded-lg max-w-[70%]">{{m.content}}</div>
        </div>
      </div>
      <div class="flex gap-2">
        <el-input v-model="input" placeholder="输入消息..." @keyup.enter="send" />
        <el-button type="primary" @click="send">发送</el-button>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref,onMounted } from "vue"
import { getSessions,sendMessage } from "../../api/cs"
const sessions = ref([])
const messages = ref([{id:1,role:"assistant",content:"您好！我是AI客服助手，有什么可以帮助您的？"}])
const input = ref(""); const currentSession = ref("")
const selectSession = (s:any)=>{currentSession.value=s.session_id;messages.value=[{id:1,role:"assistant",content:"正在为您查询..."}]}
const send = async()=>{
  if(!input.value.trim())return
  messages.value.push({id:Date.now(),role:"user",content:input.value})
  if(currentSession.value){const res=await sendMessage({session_id:currentSession.value,content:input.value});messages.value.push({id:Date.now(),role:"assistant",content:res.data.reply})}
  input.value=""
}
onMounted(async()=>{const res=await getSessions();sessions.value=res.data})
</script>
