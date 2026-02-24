const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

class ApiService {
  async fetchGuestbook() {
    const res = await fetch(`${API_URL}/api/guestbook`)
    if (!res.ok) throw new Error('Failed to fetch guestbook')
    return res.json()
  }

  async postGuestbook(entry) {
    const res = await fetch(`${API_URL}/api/guestbook`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: entry.name,
        message: entry.message
      })
    })
    if (!res.ok) throw new Error('Failed to post entry')
    return res.json()
  }

  async sendContact(contactData) {
    const res = await fetch(`${API_URL}/api/contact`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(contactData)
    })
    if (!res.ok) throw new Error('Failed to send')
    return res.json()
  }
}

export const api = new ApiService()