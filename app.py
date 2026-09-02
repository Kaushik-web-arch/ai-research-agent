"""Premium local Gradio interface for the Gemini Research Agent."""

import gradio as gr

from config import RESEARCH_PROFILES
from research_manager import ResearchManager
from styles import CSS, EXAMPLES, HEADER_HTML, JS


def mode_description(mode: str) -> str:
    profile = RESEARCH_PROFILES.get(mode, RESEARCH_PROFILES["Standard"])
    return (
        f"**{profile.name} mode** &nbsp;·&nbsp; {profile.search_count} live searches "
        f"&nbsp;·&nbsp; ≈{profile.report_word_target:,} words "
        f"&nbsp;·&nbsp; {profile.estimated_gemini_requests} free-tier Gemini requests"
    )


async def run_research(
    query: str,
    mode: str,
    audience: str,
    report_style: str,
    refresh_sources: bool,
):
    manager = ResearchManager()
    async for update in manager.run(query, mode, audience, report_style, refresh_sources):
        yield update.markdown, update.status, update.report_path


with gr.Blocks(title="AI Research Agent v2") as app:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_id="research-workspace", equal_height=False):
        with gr.Column(scale=4, min_width=330, elem_id="control-panel"):
            gr.HTML(
                """
                <div class="panel-kicker">RESEARCH BRIEF</div>
                <h2 class="panel-heading">What should we investigate?</h2>
                <p class="panel-copy">Give the agent a focused question. It will plan the work,
                search the live web, examine the evidence and write the report.</p>
                """
            )
            query_box = gr.Textbox(
                label="Research question",
                placeholder="Ask a question worth investigating…",
                lines=5,
                elem_id="research-query",
            )

            mode = gr.Radio(
                choices=list(RESEARCH_PROFILES),
                value="Standard",
                label="Research depth",
                elem_id="depth-selector",
            )
            mode_hint = gr.Markdown(mode_description("Standard"), elem_id="mode-hint")

            with gr.Row():
                audience = gr.Dropdown(
                    choices=["General", "Student", "Technical", "Decision-maker"],
                    value="General",
                    label="Audience",
                )
                report_style = gr.Dropdown(
                    choices=["Balanced", "Academic", "Action-oriented"],
                    value="Balanced",
                    label="Report style",
                )

            refresh_sources = gr.Checkbox(
                label="Force a fresh web search",
                value=False,
                info="Keep this off when repeating a question to protect your free quota.",
            )

            with gr.Row(elem_id="action-row"):
                run_button = gr.Button(
                    "Launch research  →",
                    variant="primary",
                    elem_id="research-run",
                    scale=3,
                )
                clear_button = gr.Button("Clear", variant="secondary", elem_id="research-clear", scale=1)

            with gr.Accordion("Try an example", open=False, elem_id="examples-panel"):
                gr.Examples(examples=EXAMPLES, inputs=query_box)

            gr.HTML(
                """
                <div class="privacy-card">
                  <span class="privacy-icon">⌁</span>
                  <div><strong>Private by design</strong>
                  <p>Your key stays in <code>.env</code>. Reports and cache stay on this laptop.</p></div>
                </div>
                """
            )

        with gr.Column(scale=6, min_width=420, elem_id="report-panel"):
            with gr.Row(elem_id="report-toolbar"):
                gr.HTML(
                    """
                    <div class="report-label">
                      <span class="live-dot"></span>
                      RESEARCH WORKSPACE
                    </div>
                    """
                )
                status = gr.Markdown(
                    "Ready · keyless live search standing by",
                    elem_id="research-status",
                )

            report = gr.Markdown(
                """
                <div class="empty-state">
                  <div class="empty-orbit"><span>✦</span></div>
                  <h2>Your report will appear here</h2>
                  <p>Choose a research depth, define the audience and launch the agent.</p>
                  <div class="empty-steps">
                    <span>01 · Plan</span><span>02 · Search</span><span>03 · Synthesize</span>
                  </div>
                </div>
                """,
                elem_id="research-report",
                container=True,
            )
            download = gr.File(
                label="Exported report",
                interactive=False,
                elem_id="report-download",
            )

    gr.HTML(
        """
        <footer class="app-footer">
          <span>AI Research Agent v2.4 · Kaushik Edition</span>
          <span>Gemini 3.5 Flash-Lite · live web research · local-first</span>
        </footer>
        """
    )

    mode.change(mode_description, inputs=mode, outputs=mode_hint)
    research_inputs = [query_box, mode, audience, report_style, refresh_sources]
    research_outputs = [report, status, download]
    run_button.click(run_research, inputs=research_inputs, outputs=research_outputs)
    query_box.submit(run_research, inputs=research_inputs, outputs=research_outputs)
    clear_button.click(
        lambda: (
            "",
            "Ask a question above to begin.",
            "Ready · keyless live search standing by",
            None,
        ),
        outputs=[query_box, report, status, download],
    )


if __name__ == "__main__":
    app.queue(default_concurrency_limit=1, max_size=8).launch(
        server_name="127.0.0.1",
        inbrowser=True,
        show_error=True,
        css=CSS,
        js=JS,
        theme=gr.themes.Base(primary_hue="indigo", neutral_hue="slate"),
    )
