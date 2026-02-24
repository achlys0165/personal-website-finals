const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

class ApiService {
  async fetchGuestbook() {
    const res = await fetch(`${API_URL}/guestbook`)
    const data = await res.json()
    if (!res.ok || !data.success) throw new Error(data.error || 'Failed to fetch')
    return data
  }

  async postGuestbook(entry) {
    const res = await fetch(`${API_URL}/guestbook`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: entry.name,
        message: entry.message
        // Note: removed 'from' field to match your schema
      })
    })
    const data = await res.json()
    if (!res.ok || !data.success) throw new Error(data.error || 'Failed to post')
    return data
  }

  async sendContact(contactData) {
    const res = await fetch(`${API_URL}/contact`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(contactData)
    })
    const data = await res.json()
    if (!res.ok || !data.success) throw new Error(data.error || 'Failed to send')
    return data
  }
}

export const api = new ApiService()