import api from "./index"
export const getVideos = (params?:any) => api.get("/videos",{params})
export const createVideo = (data:any) => api.post("/videos",data)
export const publishVideo = (id:number) => api.post(`/videos/${id}/publish`)
