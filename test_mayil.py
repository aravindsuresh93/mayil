import mayil as my
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

    # Create a scatter plot with Plotly
    import plotly.express as px
    import numpy as np

    # Generate some sample data
    np.random.seed(42)
    n_points = 100
    x = np.random.normal(0, 2, n_points)
    y = 0.5 * x + np.random.normal(0, 1, n_points)
    categories = np.random.choice(['A', 'B', 'C'], n_points)
    sizes = np.random.uniform(20, 60, n_points)

    # Create scatter plot
    fig = px.scatter(
        x=x, y=y,
        color=categories,
        size=sizes,
        labels={'x': 'X Axis', 'y': 'Y Axis'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Update layout for a modern look
    fig.update_traces(
        marker=dict(opacity=0.8),
        hovertemplate="<br>".join([
            "X: %{x:.2f}",
            "Y: %{y:.2f}",
            "Category: %{color}",
            "<extra></extra>"
        ])
    )

    fig.update_layout(
        plot_bgcolor='white',
        title_x=0.5,
        title_font_size=24,
        showlegend=True,
        legend_title_text='Categories',
        height=500
    )

    # Add the plot to the email
    my.plotly_chart(fig)

   




    my.header("Upcoming Events")
    my.text("Join us for our upcoming webinar on Python development.")
    my.text("Date: March 15, 2024")
    my.text("Time: 2:00 PM EST")
    
    my.divider()

    my.header("Latest Updates")
    my.text("We've added new features to our platform:", bold=True)
    my.text("- Enhanced security measures", italic=True)
    my.text("- Improved user interface", font_size=38)
    my.text("- Faster processing times", underline=True)

    my.markdown("""
                # Key Takeaways

                ## Performance Improvements
                - **30% faster** load times
                - Optimized database queries
                - Reduced memory usage

                ## New Features
                1. Real-time analytics dashboard
                2. Enhanced reporting capabilities
                3. Custom alert configurations

                > "The latest updates have significantly improved our workflow" - Lead Developer

                ### Technical Details
                | Component | Status | Notes |
                |-----------|--------|-------|
                | Backend   | ✅ Done | All tests passing |
                | Frontend  | 🚧 WIP | Final UI polish |
                | API       | ✅ Done | Documentation updated |

                Visit our [documentation](https://docs.example.com) for more details.
                """)
    
    my.show()
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