import hou

selected_node = hou.selectedNodes()[0]

if selected_node.parm('execute') is None:
    raise hou.Error("Select a Render Node!!!!")
    
elif selected_node.parm('trange').eval() != 1:
    raise hou.Error("Set Frame Range!!!!")

else:
    
    isF1Expr = selected_node.parm('f1').keyframes()
    isF2Expr = selected_node.parm('f2').keyframes()
    
    f1Expr = selected_node.parm('f1').rawValue()
    f2Expr = selected_node.parm('f2').rawValue()

    start_frame = int(selected_node.parm('f1').eval())
    end_frame = int(selected_node.parm('f2').eval())
    num_tasks = end_frame - start_frame+1

    with hou.InterruptableOperation(
            "Performing Tasks", open_interrupt_dialog=True) as operation:
        for i in range(num_tasks):
            #
            # PERFORM TASK HERE.
            #
            
            index = start_frame + i
            
            selected_node.parm('f1').set(index)
            selected_node.parm('f2').set(index)
            selected_node.parm('execute').pressButton()
            
    
            # Update operation progress.
            percent = float(i) / float(num_tasks)
            operation.updateProgress(percent)
            
    if isF1Expr != ():
        selected_node.parm('f1').setExpression(f1Expr)
    else:
        selected_node.parm('f1').set(start_frame)
        
    if isF2Expr != ():
        selected_node.parm('f2').setExpression(f2Expr)
        selected_node.parm('f2').set(end_frame)
