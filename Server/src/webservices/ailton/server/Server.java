package webservices.ailton.server;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

import org.json.JSONArray;
import org.json.JSONObject;

public class Server {

	private static int numeroAlunosMatriculados(JSONArray alunos) {
		int numeroAlunosMatriculados = 0;

		for (int i = 0; i < alunos.length(); i++) {
			if (alunos.getJSONObject(i).getBoolean("matriculado") == true) {
				numeroAlunosMatriculados++;
			}
		}

		return numeroAlunosMatriculados;
	}

	private static void exibirDadosTurmas(JSONObject turmas) {
		// Percorrendo as turmas.
		turmas.getJSONArray("turmas").forEach(item -> {
			JSONObject turma = (JSONObject) item;

			System.out.printf(
					"\nA turma %s de %d do curso %s possui %d alunos, dos quais %d estão devidamente matriculados.\n",
					turma.getString("nome"), turma.getInt("ano"), turma.getString("curso"),
					turma.getJSONArray("alunos").length(), numeroAlunosMatriculados(turma.getJSONArray("alunos")));
		});
	}

	private static void server() {
		final int SERVER_PORT = 12000;

		// Iniciando o servidor
		try (ServerSocket server_socket = new ServerSocket(SERVER_PORT)) {
			System.out.printf("Servidor ouvindo a porta %d\n", SERVER_PORT);
			while (true) {
				// Esperando a conexão de um cliente.
				Socket connection_socket = server_socket.accept();
				System.out.println("Cliente conectado: " + connection_socket.getInetAddress().getHostAddress());

				// Recebendo a mensagem do cliente.
				BufferedReader br = new BufferedReader(new InputStreamReader(connection_socket.getInputStream(), StandardCharsets.UTF_8));
				JSONObject turmas = new JSONObject(br.readLine());
				exibirDadosTurmas(turmas);

				System.out.println("\n");
				br.close();
				connection_socket.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		server();
	}

}
