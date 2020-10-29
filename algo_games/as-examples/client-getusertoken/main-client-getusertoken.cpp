///#################################
/// Author: Martin Wistauder
/// Date: 12.10.2020
/// Version: 1.1
///#################################
#include <iostream>
#include <memory>
#include <netcode.grpc.pb.h>
#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>

typedef std::unique_ptr<netcode::GameCom::Stub> StubPtr;

class Settings
{
	public:
		std::string matrNr = "11819382";    // Insert your matr.number here
		std::string secret = "creator";    // Don't use any personal passwords
};

int getUserToken();

StubPtr stub;
Settings settings;

int main()
{
	// connect to the server
	std::string host = "gameserver.ist.tugraz.at:80";
	auto channel = grpc::CreateChannel(host, grpc::InsecureChannelCredentials());

	// wait till we connect or timeout after 5 seconds
	if (!channel->WaitForConnected(gpr_time_add(
			gpr_now(GPR_CLOCK_REALTIME),
			gpr_time_from_seconds(5, GPR_TIMESPAN))))
	{
		std::cout << "Error: Connection Timeout.\n";
		return 1;
	}

	// create a stub
	stub = netcode::GameCom::NewStub(channel);

	return getUserToken();
}

int getUserToken()
{
	// create the request
	netcode::AuthPacket authPacket;
	authPacket.set_matr_number(settings.matrNr);
	authPacket.set_secret(settings.secret);

	// create required objects to use the rpc
	netcode::GetUserTokenResponse response;
	grpc::ClientContext context; // NOTE: after a rpc uses the client context, it gets invalidated and cannot be reused

	// call the remote procedure from the stub
	grpc::Status status = stub->GetUserToken(&context, authPacket, &response);

	// check the response status
	if (!status.ok())
	{
		std::cout << "Error: The request has been canceled by the server.\n";
		return 1;
	}

	std::cout << response.user_token() << "\n";

	return 0;
}