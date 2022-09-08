# houdini_rendering_frame_by_frame
This is a tool to render your image frame by frame in Houdini

In some occasion, FX artists may find that Houdini crashes for unknown reason when rendering sequences, but rendering single frame works fine. So, I write a small script to render the whole sequence frame by frame. To use the script, just create a new shelf tool and paste the codes into the tool, then select a render node, click the tool. An interruptable process bar will pop up during the rendering process.
