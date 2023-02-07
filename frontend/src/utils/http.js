import axios from 'axios';
import router from "../router";

const instance = axios.create({
    // baseURL: import.meta.env.VITE_BACKEND_HOST
    baseURL: 'http://localhost:9090'
});

instance.interceptors.request.use((config) => {
    const token = localStorage.getItem('token')

    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }

    return config
})

instance.interceptors.response.use(undefined, (error) => {
    if (error.response?.status === 401) {
        router.push('/login')
    }

    return Promise.reject(error)
})

export default instance
