import mayil as my
import pandas as pd

def create_sample_email():
    # Build the email content
    my.title("Welcome to Our Newsletter")

    # Build the email content
    my.header("Welcome to Our Newsletter")
    my.subheader("We're excited to share our latest updates with you!")

    my.text("""Lorum Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""", justify=True)


    my.metric("Total Users", 1000)

    my.caption("This is a caption")

    t = "Lorum Ipsum is simply dummy text of the printing and typesetting industry."

    my.sticky_note("Sticky Note", t, color="yellow")

    cols = my.columns(3)
    with cols[0]:
        my.metric("Total Users", 1000)
        my.sticky_note("Sticky Note 2", t, color="blue")
        
    with cols[1]:
        my.metric("Total Users", 1002)
        my.header('yayy')
        my.caption("This is a caption")
    with cols[2]:
        my.metric("Total Users", 1001)
        my.sticky_note("Sticky Note 3", t, color="green")
        
    df = pd.DataFrame({
        'ID': [1, 2, 3],
        'Name': ['John', 'Jane', 'Bob'], 
        'Age': [25, 30, 35],
        'Timestamp': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'Score': [95.5, 88.3, 92.1],
        'Active': [True, False, True]
    })
    my.table(df)
    my.hyperlink("Click here", "https://www.google.com")

    # Test ftable with conditional formatting
    conditions = {
        'Score': [
            (lambda x: x < 90, '#ff0000'),  # Red if < 90
            (lambda x: x >= 90, '#00ff00')  # Green if >= 90
        ],
        'Active': [
            (lambda x: x == True, '#00ff00'),  # Green if active
            (lambda x: x == False, 'blue')  # Red if inactive
        ],
        'Timestamp': [
            (lambda x: x < pd.Timestamp('2024-01-02'), '#ff0000'),  # Red if before Jan 2
            (lambda x: x >= pd.Timestamp('2024-01-02'), '#00ff00')  # Green if Jan 2 or later
        ]
    }

    # Test with cell background colors
    my.ftable(df, cell_colors=conditions)

    # Test with text colors
    my.ftable(df, text_colors=conditions)

    my.header("Upcoming Events")
    my.text("Join us for our upcoming webinar on Python development.")
    my.text("Date: March 15, 2024")
    my.text("Time: 2:00 PM EST")
    
    my.divider()

    my.header("Latest Updates")
    my.text("We've added new features to our platform:")
    my.text("- Enhanced security measures")
    my.text("- Improved user interface")
    my.text("- Faster processing times")
    
    return my

def save_to_file(html_content, filename="sample_email.html"):
    with open(filename, "w") as f:
        f.write(html_content)
    print(f"Email saved to {filename}")

if __name__ == "__main__":
    # Create the email
    create_sample_email()
    
    # Get the HTML content
    html_content = my.body()
    
    # Save to file
    save_to_file(html_content)
    
    print("\nEmail preview:")
    # print("-" * 50)
    # print(html_content)
    # print("-" * 50) 