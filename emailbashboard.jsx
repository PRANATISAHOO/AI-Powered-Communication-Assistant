function handleResolve(emailId) {
    axios.post("/resolve", { email_id: emailId }).then(() => {
      alert("Email marked as resolved");
      window.location.reload(); // Refresh to show updated status
    });
  }
  {emails.map((email, idx) => (
    <div key={idx} className="email-card">
      <p><strong>From:</strong> {email.from}</p>
      <p><strong>Subject:</strong> {email.subject}</p>
      <p><strong>Sentiment:</strong> {email.sentiment}</p>
      <p><strong>Urgency:</strong> {email.urgency}</p>
      <p><strong>Response:</strong> {email.response}</p>
      <button onClick={() => handleResolve(email._id)}>Mark as Resolved</button>
    </div>
  ))}
  import { Card, CardContent, Typography, Button } from '@mui/material';

{emails.map((email, idx) => (
  <Card key={idx} style={{ marginBottom: '20px' }}>
    <CardContent>
      <Typography variant="h6">{email.subject}</Typography>
      <Typography variant="body2">From: {email.from}</Typography>
      <Typography variant="body2">Sentiment: {email.sentiment}</Typography>
      <Typography variant="body2">Urgency: {email.urgency}</Typography>
      <Typography variant="body2">Response: {email.response}</Typography>
      <Button variant="contained" color="primary" onClick={() => handleResolve(email._id)}>
        Mark as Resolved
      </Button>
    </CardContent>
  </Card>
))}

  