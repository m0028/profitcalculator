This is an experiment to make a simple profit calculator.
It answers the question: when I buy at this price, and sell at this other price, what is my profit margin % ?
You can set a target profit margin in % and it will advise both a better sell price or buy price to meet stated target if the target % is not met.

Should run on localhost:9001 standard, you can change this of course

These requirements were used in the Claude Opus prompt

Certainly! Here's a comprehensive list of all the requirements for your profit calculator app:

1. The app should be optimized for mobile devices.
2. Users can enter two numbers: the buy price and the sell price.
3. The app will automatically calculate and display the profit percentage (Sell-Buy) as a percentage of Buy when the user enters the prices.
4. The app allows users to set a target profit margin under settings, which is defaulted to 30%.
5. The app will display the adjusted buy price and sell price next to the entered prices, which would lead to the target profit margin.
   - If the current profit margin is below the target, the app will show the adjusted buy price (calculated as Sell / (1 + Target Profit Margin)) next to the buy price field.
   - If the current profit margin is below the target, the app will show the adjusted sell price (calculated as Buy * (1 + Target Profit Margin)) next to the sell price field.
6. The app should follow iPhone-like layout and Apple design principles, using an appropriate color scheme.
7. The port number should be easily editable in the Python code and listed as a constant at the top of the file. It should be set to a free port number on macOS (e.g., 9001).
8. The inputted buy and sell prices should remain visible after the calculation is done, always showing the latest input entered by the user.
9. The app should calculate and display the results in real-time as the user types/enters/inputs the buy and sell prices, eliminating the need for a separate "Calculate Profit" button.
10. The app should be containerized using Docker for easy deployment and portability.
11. The app should be deployed on a ... VPS (Virtual Private Server) with the IP address xx.xx.xxx.xxx
12. The app should be accessible via the subdomain ..., which should be pointed to the Hetzner VPS IP address using an A record in the DNS settings.
13. The app should be running inside a Docker container on the Hetzner VPS, with the container port 9001 mapped to the host port 9001.
14. The Docker container should be configured to always restart unless explicitly stopped, ensuring high availability.
15. Nginx should be installed on the Hetzner VPS and configured as a reverse proxy to forward requests from ... to the Docker container running on localhost:9001.
16. The app should be accessible via HTTPS using a free SSL/TLS certificate obtained from Let's Encrypt using Certbot.
17. The app's main Python file should be named percentageprofit.py.
18. The requirements.txt file should specify the necessary dependencies, including Flask.
19. The project structure should include the following files:
    - Dockerfile
    - percentageprofit.py
    - requirements.txt
    - templates/
      - index.html
      - settings.html
20. The app should use green color when the entered prices lead to a profit margin equal to or greater than the target profit margin, and red color when the prices do not meet the target.
21. The recommended prices should be displayed to the right of the input fields only when the entered prices lead to a profit margin that is not equal to or smaller than the target margin.
22. The size of the elements should be increased to better fit an iPhone screen while still ensuring everything fits within the screen.
23. The input boxes should not resize as the user types.

These requirements cover the functionality, design, deployment, and accessibility aspects of your profit calculator app. Let me know if you have any questions or if there's anything else you'd like to add or modify in the requirements.


