"""Supervisor of the Line Following benchmark."""

from controller import Supervisor
import os
import sys

try:
    includePath = os.environ.get("WEBOTS_HOME") + "/projects/samples/robotbenchmark/include"
    includePath.replace('/', os.sep)
    sys.path.append(includePath)
    from robotbenchmark import robotbenchmarkRecord
except ImportError:
    sys.stderr.write("Warning: 'robotbenchmark' module not found.\n")
    sys.exit(0)

robot = Supervisor()

timestep = int(robot.getBasicTimeStep())

# Retorna um identificador para um nó no mundo a partir de seu nome DEF.
l1r2 = robot.getFromDef("L1R2")

# A função recupera um manipulador para um campo de nó. O campo é especificado por seu nome em field_name e o nó ao qual pertence. 
translation = l1r2.getField("translation")

running = True
stopMessageSent = False
while robot.step(timestep) != -1:
    # As funções wb_supervisor_field_get_sf_* recuperam o valor de um campo único especificado (SF). O tipo do campo deve 
    # corresponder ao nome da função utilizada, caso contrário o valor de retorno é indefinido (e uma mensagem de aviso é exibida). 
    t = translation.getSFVec3f()
    if running:
        time = robot.getTime()        
        if ((t[2] > 1.60 and t[2] < 1.75) and (t[0] > 1.26 and t[0] < 1.75)):
            message = "stop"
            running = False
        
        # Essas funções permitem que o controlador do robô se comunique com uma janela de robô HTML. 
        robot.wwiSendText("time:%-24.3f" % time)
    else:  # aguarde a mensagem de gravação
        if not stopMessageSent:
            robot.wwiSendText("stop")
            stopMessageSent = True
        else:
            message = robot.wwiReceiveText()
            if message:
                if message.startswith("record:"):
                    record = robotbenchmarkRecord(message, "line_following", -time)
                    robot.wwiSendText(record)
                    break
                elif message == "exit":
                    break

# O modo de simulação atual também pode ser modificado pelo usuário do Webots, ao clicar nos botões correspondentes 
# na interface do usuário.
robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
