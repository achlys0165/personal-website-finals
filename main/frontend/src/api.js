import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:5000'

const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Request interceptor
api.interceptors.request.use(config => {
  return config
}, error => {
  return Promise.reject(error)
})

// Response interceptor
api.interceptors.response.use(response => {
  return response
}, error => {
  console.error('[API Error]', error.response?.data || error.message)
  return Promise.reject(error)
})

export const guestlistAPI = {
  getEntries: () => api.get('/api/guestlist'),
  postEntry: (data) => api.post('/api/guestlist', data),
}

export default api
