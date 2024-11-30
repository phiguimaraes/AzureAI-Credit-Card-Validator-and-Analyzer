<h1>Credit Card Validator and Information Extractor</h1>

<p>This project allows you to upload a JPEG, PNG, or JPG image of a credit card. The system will analyze the image, validate if it's a credit card, and if so, extract and display the credit card information.</p>

<br> 

<h3>Features</h3>
<ul>
  <li>Upload a JPEG image of a credit card.</li>
  <li>Analyze the image to detect if it's indeed a credit card.</li>
  <li>Extract information such as the cardholder's name, card number, issuing bank, expiration date, and CVV.</li>
  <li>Display the extracted information in a user-friendly format.</li>
</ul>

<br> 

<h3>Tech Stack</h3>
<ul>
  <li>Azure AI: Uses Azure's Document Intelligence services to analyze and extract data from credit card images.</li>
  <li>Streamlit: For building the user interface.</li>
  <li>Azure Blob Storage: To upload and store the images.</li>
</ul>

<br>

<h3>How It Works</h3>
<p>The uploaded image is sent to Azure Blob Storage.</p>
<p>The image URL is then passed to Azure’s Document Intelligence API for analysis.</p>
<p>If the document is recognized as a credit card, the relevant information is extracted and displayed.</p>

<br> 

<h3>Example Output</h3>
<p>Cardholder Name: John Doe</p>
<p>Card Number: 1234 5678 9876 5432</p>
<p>Issuing Bank: Bank of Example</p>
<p>Expiration Date: 12/25</p>
<p>CVV: 123</p>
