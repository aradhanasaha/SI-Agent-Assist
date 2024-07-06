def get_history1(context):
    [
                                {
                                    "role": "user",
                                    "parts": context
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Can I buy multiple products in one order?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Yes, you can buy multiple products in one order. Simply add the items to your cart and proceed to checkout."
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Alright, can you guide me to find the cart?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Sure, you can open your mobile app and then on to the at-most right you would find cart symbol."
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Can I get a GST invoice for my order?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Hello! Yes, you can obtain a GST invoice. You can provide your GST details at checkout or contact customer support with your order number and GST details after purchase. Thank you!"
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Can you guide me with my electronics item which is under warranty but not working?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Hello! For warranty service, please contact our customer support team with your order number and a description of the issue. We will guide you through the process for repair or replacement. Thank you!"
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Okay, I want to get it repaired. Can you help me with that?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Hello! Sure, please provide your order number and issue details. We will arrange for the repair service under warranty. Thank you!"
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Okay, so my order number is XXXXXXX and that was a laptop which is not starting."
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Alright, Would Thursday be suitable for you to come to your nearest shop? If yes would book your slot."
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Yes so Thursday seems fine to me. Thank you!"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Happy to help. Let me know if have any other questions."
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Hello, I am willing to buy an earbuds but I find it very expensive at your store and am getting a good price somewhere else. Could you please look into it? "
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer."
                                    ]
                                },
                                {
                                    "role": "model",
                                    "parts": [
                                        "Okay so I got this offer at a XYZ company which is giving me 30% discount based on the my credit score. "
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer."
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Hello, How are you? "
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "I am good but I need some questions to be answered related to your product policies?"
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Sure, go ahead. Feel free to ask anything. I will be happy to help."
                                    ]
                                },
                                {
                                    "role": "user",
                                    "parts": [
                                        "Alright. My question is What is the EMI policies of the product category of electronics?"
                                    ]
                                }
                            ]
    
def get_history2(context):
     [
                        {
                            "role": "user",
                            "parts": context,
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Hello, I am here to assist you with your queries related to the policies of our ecommerce company. Please feel free to ask."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Can I get a GST invoice for my order?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Yes, you can obtain a GST invoice. Provide your GST details at checkout or contact customer support with your order number and GST details after purchase. Thank you! \n Recommendation 2: Hello! You can get a GST invoice by providing your GST number during checkout. If missed, contact customer support with your order and GST details to get the invoice. Thank you!\n Recommendation 3: Hello! To get a GST invoice, provide your GST number during checkout. If missed, contact customer support with your order number and GST details, and we’ll send you the invoice. Thank you!"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Can you guide me with my electronics item which is under warranty but not working?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Please contact our customer support with your order number and issue details. We will assist you with warranty service and repair or replacement options. Thank you! \n Recommendation 2: Hello! For warranty service, please contact our customer support team with your order number and a description of the issue. We will guide you through the process for repair or replacement. Thank you!\n Recommendation 3: Hello! For warranty assistance, provide issue details and order number with necessary details. You can then proceed with either repairement or replacement. "
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Okay, I want to get it repaired. Can you help me with that?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! Sure, please provide your order number and issue details. We will arrange for the repair service under warranty. Thank you! \n Recommendation 2: Hello! Absolutely, please share your order number and a brief description of the issue. We will schedule a repair service and provide further instructions. Thank you!\n Recommendation 3: Hello! To proceed with the repair. Kindly provide your order details. We will schedule an appointment for you."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How can I apply for an EMI?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! To apply for an EMI, choose the EMI option during checkout and select your preferred bank and plan. Thank you! \n Recommendation 2: Hello! You can apply for an EMI during the checkout process by selecting the EMI payment option. Choose your bank and preferred EMI plan, then complete the payment. Thank you!\n Recommendation 3: Hello! Select the EMI option at checkout, choose your bank and plan, and complete the payment. Thank you!"
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Hello, I am willing to buy an earbuds but I find it very expensive at your store and am getting a good price somewhere else. Could you please look into it? "
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Thank you for reaching out. We offer top-quality products with excellent customer service, including warranties and easy returns. Can you provide the price you found elsewhere?\n Recommendation 2: Thank you for your message. We may be able to match the price you've found. Please share the details of the other offer. \n Recommendation 3: Thank you for your concern. Have you checked our current promotions? We offer benefits like free shipping, loyalty points, and extended warranties. Let me know if you need assistance."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "Okay so I got this offer at a XYZ company which is giving me 30% discount based on the my credit score. "
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Thank you for sharing this. We can offer a similar discount based on your credit score. Please provide the details, and we’ll proceed. \n Recommendation 2: Thank you for the info. We strive to offer competitive pricing. Let’s review your credit score to see if we can match or improve on this offer. \n Recommendation 3: Thank you for the update. We offer various discounts and financing options. Let's check your eligibility for similar or better deals."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How do I know my order has been confirmed?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! You will receive an email confirmation with your order details shortly after placing your order. Thank you!\n Recommendation 2: Hello! After placing your order, you will receive an email confirmation with all the details. You can also check your order status in your account on our website. Thank you! \n Recommendation 3: Hello! You can check your mail, you would have received a mail regading confirmation."
                            ]
                        },
                        {
                            "role": "user",
                            "parts": [
                                "How can I apply for an EMI?"
                            ]
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Recommendation 1: Hello! To apply for an EMI, choose the EMI option during checkout and select your preferred bank and plan. Thank you!\n Recommendation 2: Hello! You can apply for an EMI during the checkout process by selecting the EMI payment option. Choose your bank and preferred EMI plan, then complete the payment. Thank you! \n Recommendation 3: Hello! Select the EMI option at checkout, choose your bank and plan, and complete the payment. Thank you!"
                            ]
                        }
                    ]