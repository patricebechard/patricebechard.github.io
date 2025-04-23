document.addEventListener('DOMContentLoaded', function() {
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
    
    // Configure marked options
    marked.setOptions({
        gfm: true,
        breaks: true,
        headerIds: false,
        mangle: false
    });

    // Helper function to ensure proper line breaks
    function preprocessMarkdown(text) {
        // Ensure paragraphs have proper spacing
        return text.split('\n').map(line => {
            // Preserve empty lines
            if (line.trim() === '') return '';
            // Add two spaces at the end of each non-empty line for markdown line breaks
            return line.trim() + '  ';
        }).join('\n');
    }

    // Toggle reasoning content when header is clicked
    reasoningHeader.addEventListener('click', function() {
        if (expandArrow.style.display === 'inline-block') {
            reasoningContent.style.display = reasoningContent.style.display === 'none' ? 'block' : 'none';
            expandArrow.innerHTML = reasoningContent.style.display === 'none' ? '▼' : '▲';
        }
    });

    function startStreaming() {
        if (hasStartedStreaming) return;
        hasStartedStreaming = true;

        reasoningTitle.textContent = 'Reasoning';
        reasoningTitle.style.fontWeight = 'bold';
        thinkingSpinner.style.display = 'none';
        expandArrow.style.display = 'inline-block';
        
        const content = textInput.value;
        let accumulatedText = '';
        let i = 0;

        function streamText() {
            if (i < content.length) {
                accumulatedText += content[i];
                try {
                    // Preprocess the text and render markdown
                    const processedText = preprocessMarkdown(accumulatedText);
                    streamingText.innerHTML = marked.parse(processedText);
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

    setTimeout(startStreaming, 3000);

    // Fallback
    setTimeout(function() {
        if (!hasStartedStreaming) {
            console.log('Forcing stream start due to timeout');
            startStreaming();
        }
    }, 5000);
});