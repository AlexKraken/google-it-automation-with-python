#!/usr/bin/env python3

import os, sys
from datetime import date
import reports
import emails


def main(argv):
    attachment = r"/tmp/processed.pdf"
    title = f"Processed Update on {date.today()}"
    paragraph = ""

    source = r"supplier-data/descriptions"

    for filename in os.listdir(source):
        name, extension = os.path.splitext(filename)
        if extension == ".txt":
            with open(os.path.join(source, filename)) as input_file:
                fruit_name = input_file.readline()
                fruit_weight = input_file.readline()

                paragraph += (
                    "name: "
                    + fruit_name
                    + "<br/>weight: "
                    + fruit_weight
                    + "<br/>"
                    + "\n<br/>"
                )

    print(paragraph)

    reports.generate_report(attachment, title, paragraph)
    sender = "<example.sender@email.com>"
    recipient = "<example.recipient@email.com>"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = attachment

    message = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
