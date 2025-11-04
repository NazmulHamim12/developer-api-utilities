#🔹 Hamim’s Developer Utility API 🚀

আমার ছোটখাটো API বানালাম, যেটা ডেভেলপারদের everyday কাজকে আরও easy করে দেবে। এখানে কী কী করতে পারো:

UUID বানানো

একদম unique ID চাইলে, এই endpoint দিয়ে সহজেই বানাতে পারবে।

Example: /uuid

Output: b2d3f6a4-...

Timestamp দেখানো

এখন সময় কত, seconds হিসেবে বা readable format-এ।

Example: /timestamp

Output: 169xxxxxx + 2025-11-05 00:00:00

Random Color

ওয়েব বা app design এ random color দরকার হলে।

Example: /random-color

Output: #a3f4d2

Random Password

Strong password বানাতে সাহায্য করে।

Example: /random-password?length=12

Output: p9$Klm2@!qz4

Random String

Test বা temporary key বানানোর জন্য।

Example: /random-string?length=10

Output: abcdxyzpqr

Text Hash করা

Text কে md5 বা sha256 hash করতে চাও? সহজেই করা যায়।

Example: /hash-string (POST) { "text":"hello" }

Output: 2cf24dba...

Email Validation

Check করবে email ঠিক আছে কিনা, Gmail কিনা, এবং min 6 character আছে কিনা।

Example: /validate-email (POST) { "email":"test@gmail.com" }

Output: true/false

IP Address দেখানো

নিজের বা request এর IP জানতে।

Example: /ip-info

Output: 123.45.67.89

Date Info

আজকের date, day, month, year, এবং time।

Example: /date-info

Output: 2025-11-05, Thursday, 00:05:12

Random Number

Min-max range এর মধ্যে random number।

Example: /random-number?min=1&max=100

Output: 42

Random Quote

Motivational বা funny quote randomly পাওয়া যাবে।

Example: /quote

Output: "Talk is cheap. Show me the code." – Linus Torvalds
