import api from "./index"
export const getLeads = (params?:any) => api.get("/leads",{params})
export const createLead = (data:any) => api.post("/leads",data)
export const getLeadScore = (id:number) => api.get(`/leads/${id}/score`)
