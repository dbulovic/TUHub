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
		std::string pseudonym = "BloodAndAshes"; // Your group pseudonym
};

StubPtr stub;
Settings settings;

int setPseudonym();

int main()
{
	// create a channel (which connects to the server)
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

	return setPseudonym();
}

int setPseudonym()
{
	// create the request
	netcode::SetPseudonymRequest request;
	auto auth = new netcode::AuthPacket();
	auth->set_matr_number(settings.matrNr);
	auth->set_secret(settings.secret);
	request.set_allocated_auth(auth);
	request.set_pseudonym(settings.pseudonym);

	// create required objects to use the rpc
	netcode::SetPseudonymResponse response;
	grpc::ClientContext context; // NOTE: after a rpc uses the client context, it gets invalidated and cannot be reused

	// call the remote procedure from the stub
	grpc::Status status = stub->SetGroupPseudonym(&context, request, &response);

	// check the response status
	if (!status.ok())
	{
		std::cerr << "Error: The request has been canceled by the server.\n";
		return 1;
	}

	// check the response error code
	switch (response.error_code())
	{
		case netcode::SetPseudonymResponse_ErrorCode_UNDEFINED_ERROR:
			std::cerr << "Error: An undefined error occurred.\n";
			break;
		case netcode::SetPseudonymResponse_ErrorCode_OK:
			std::cout << "Setting pseudonym was successful!\n";
			break;
		case netcode::SetPseudonymResponse_ErrorCode_REQUEST_REJECTED:
			std::cerr << "Error: Request rejected.\n";
			break;
		case netcode::SetPseudonymResponse_ErrorCode_ALREADY_USED:
			std::cerr << "Error: Pseudonym already in use.\n";
			break;
		case netcode::SetPseudonymResponse_ErrorCode_TOO_LONG:
			std::cerr << "Error: Pseudonym too long.\n";
			break;
		case netcode::SetPseudonymResponse_ErrorCode_EMPTY_FIELDS:
			std::cerr << "Error: Empty fields.\n";
			break;
		default:
			std::cerr << "Error: Received an unknown error code\n";
			break;
	}

	return 0;
}