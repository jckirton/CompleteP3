from diagrams import Diagram
import diagrams.programming.flowchart as flowchart

with Diagram(
    "Flowchart Name",
    autolabel=True,
    # direction="TB",
    show=False,
    # curvestyle="curved"
):
    (
        flowchart.StartEnd()
        >> [
            flowchart.StartEnd(),
            flowchart.Database(),
            flowchart.StartEnd(),
            flowchart.StartEnd(),
        ]
        >> flowchart.Collate()
    )
