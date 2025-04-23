document.addEventListener('DOMContentLoaded', function() {
    // Add a flag to track if streaming has started
    let hasStartedStreaming = false;

    // Get elements
    const reasoningBox = document.getElementById('reasoning-box');
    const reasoningHeader = document.getElementById('reasoning-header');
    const reasoningTitle = document.getElementById('reasoning-title');
    const thinkingSpinner = document.getElementById('thinking-spinner');
    const expandArrow = document.getElementById('expand-arrow');
    const reasoningContent = document.getElementById('reasoning-content');
    const streamingText = document.getElementById('streaming-text');
    const textInput = document.getElementById('textInput');
    const cursor = document.querySelector('.blinking-cursor');
    
    // Toggle reasoning content when header is clicked
    reasoningHeader.addEventListener('click', function() {
        if (expandArrow.style.display === 'inline-block') {
            reasoningContent.style.display = reasoningContent.style.display === 'none' ? 'block' : 'none';
            expandArrow.innerHTML = reasoningContent.style.display === 'none' ? '▼' : '▲';
        }
    });

    // Function to start the streaming process
    function startStreaming() {
        if (hasStartedStreaming) return; // Prevent multiple starts
        hasStartedStreaming = true;

        reasoningTitle.textContent = 'Reasoning';
        reasoningTitle.style.fontWeight = 'bold';
        thinkingSpinner.style.display = 'none';
        expandArrow.style.display = 'inline-block';
        
        // Start streaming the text
        const content = textInput.value;
        let accumulatedText = '';
        let i = 0;

        function streamText() {
            if (i < content.length) {
                accumulatedText += content[i];
                try {
                    // Use marked with options
                    streamingText.innerHTML = marked.parse(accumulatedText, {
                        gfm: true,
                        breaks: true
                    });
                } catch (e) {
                    console.error('Markdown parsing error:', e);
                    streamingText.textContent += content[i];
                }
                i++;
                setTimeout(streamText, 2);
            } else {
                cursor.style.display = 'none';
            }
        }
        streamText();
    }

    // Start streaming after a short delay
    setTimeout(startStreaming, 3000);

    // Fallback: If streaming hasn't started after 5 seconds, force start it
    setTimeout(function() {
        if (!hasStartedStreaming) {
            console.log('Forcing stream start due to timeout');
            startStreaming();
        }
    }, 5000);
});