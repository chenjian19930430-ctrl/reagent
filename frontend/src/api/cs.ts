import api from "./index"
export const sendMessage = (data:any) => api.post("/cs/messages",data)
export const getSessions = () => api.get("/cs/sessions")
export const searchKnowledge = (query:string) => api.get("/cs/knowledge-base",{params:{query}})
