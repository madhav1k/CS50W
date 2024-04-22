document.addEventListener('DOMContentLoaded', function() {

  const emailDetailView = document.createElement('div');
  emailDetailView.setAttribute('id', 'email-detail-view');
  document.querySelector('.container').append(emailDetailView);

  document.querySelector('#archived').innerHTML = "Archive";

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Submit handler
  document.querySelector("#compose-form").addEventListener('submit', send_email);
  
  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-detail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  // Add submit button margin
  let submit = document.querySelector('.btn-primary');
  submit.className = "btn btn-primary my-3";
}

function view_email(id) {

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-detail-view').style.display = 'block';
    document.querySelector('#email-detail-view').innerHTML = `
      <ul class="list-group">
        <li class="list-group-item"><strong>From:</strong> ${email.sender}</li>
        <li class="list-group-item"><strong>To:</strong> ${email.recipients}</li>
        <li class="list-group-item"><strong>Subject:</strong> ${email.subject}</li>
        <li class="list-group-item"><strong>Timestamp:</strong> ${email.timestamp}</li>
      </ul>
    `;

    // Change to read
    if (!email.read) {
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true,
        }),
      });
    }
    
    // Archive/Unarchive logic
    const user_email = document.querySelector('h2').innerHTML;
    if (email.sender != user_email) {
      let btn_arch = document.createElement('button');
      btn_arch.innerHTML = email.archived ? "Unarchive" : "Archive";
      btn_arch.className = email.archived ? "btn btn-sm btn-outline-secondary my-3" : "btn btn-sm btn-outline-secondary my-3";
      btn_arch.addEventListener('click', function() {
        fetch(`/emails/${id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !email.archived,
          }),
        })
        .then(() => load_mailbox('inbox'))
      });
      document.querySelector('#email-detail-view').append(btn_arch);
    }

    //Reply logic
    let btn_reply = document.createElement('button');
    btn_reply.innerHTML = "Reply";
    btn_reply.className = "btn btn-sm btn-outline-secondary mx-1 my-3";
    btn_reply.addEventListener('click', function() {
      compose_email();
      document.querySelector('#compose-recipients').value = email.sender;
      let subject = email.subject;
      if (subject.split(' ', 1)[0] != "Re:") {
        subject = "Re: " + subject;
      }
      document.querySelector('#compose-subject').value = subject;
      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
    });
    document.querySelector('#email-detail-view').append(btn_reply);

    //Email body
    let emailBody = document.createElement('div');
    emailBody.innerHTML = `${email.body}`;
    emailBody.className = "list-group-item";
    document.querySelector('#email-detail-view').append(emailBody);
  });
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-detail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get the emails for that mailbox and user
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Loop through emails and create a div for each
    emails.forEach(singleEmail => {
      let container = document.createElement('div');
      container.className = "container";
      document.querySelector('#emails-view').append(container);

      // Create div for each email
      let newEmail = document.createElement('div');
      newEmail.className = "row";
      newEmail.style.border = "1px solid black";
      newEmail.innerHTML =`
        <div class="my-2 col-2"><strong>${singleEmail.sender}</strong></div>
        <div class="my-2 col">${singleEmail.subject}</div>
        <div class="my-2 col-3 text-muted text-right">${singleEmail.timestamp}</div>
      `;
      
      // Change background-color
      if (singleEmail.read) {
        newEmail.style.backgroundColor = "#f2f2f2";
      }
      else {
        newEmail.style.backgroundColor = "#ffffff";
      }

      // Add click event to view email
      newEmail.addEventListener('click', function() {
        view_email(singleEmail.id);
      });
      document.querySelector('#emails-view .container').append(newEmail);
    });
  });
}

function send_email(event) {

  event.preventDefault();

  // Store fields
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  // Send data to backend
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients, 
      subject: subject, 
      body: body,
    }),
  })
  .then(() => {
    load_mailbox('sent');
  });
}