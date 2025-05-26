from rest_framework.views import APIView
from rest_framework.response import Response
import subprocess
from core.models import Terminal

class CreateTerminalView(APIView):
    def post(self, request):
        command = request.data.get('command')

        if not command:
            return Response({'status': 'error', 'message': 'Command is required'}, status=400)

        try:
            terminal = Terminal.objects.create(commands=command)
            
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            
            return Response({
                'status': 'success',
                'message': 'Command executed',
                'pid': process.pid,
                'stdout': stdout,
                'stderr': stderr,
                'terminal_id': terminal.id
            }, status=201)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=500)
