import qrcode

image = qrcode.make("https://www.linkedin.com/in/vishwajeet-kumar-singh-760413171/")

image.save("LinkedInProfile(Vishwajeet).png")