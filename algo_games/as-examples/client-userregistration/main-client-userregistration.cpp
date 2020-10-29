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
		std::string email = "david.bulovic@student.tugraz.at";     // Insert your @student.tugraz.at email here
		std::string fullname = "David Bulovic";  // Insert your firstname and surname here
		std::string matrNr = "11819382";    // Insert your matr.number here
		std::string secret = "creator";    // Don't use any personal passwords
};

Settings settings; // this is global for no reason
StubPtr stub;

int registration();

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

	return registration();
}

int registration()
{
	// create the request
	netcode::UserRegistrationRequest request;
	request.set_email(settings.email);
	request.set_fullname(settings.fullname);
	request.set_matr_number(settings.matrNr);
	request.set_secret(settings.secret);

	// create required objects to use the rpc
	netcode::UserRegistrationResponse response;
	grpc::ClientContext context; // NOTE: after a rpc uses the client context, it gets invalidated and cannot be reused

	// call the remote procedure from the stub
	grpc::Status status = stub->UserRegistration(&context, request, &response);

	// check the response status
	if (!status.ok())
	{
		std::cerr << "Error: The request has been canceled by the server.\n";
		return 1;
	}

	// check the response error code
	switch (response.error_code())
	{
		case netcode::UserRegistrationResponse_ErrorCode_UNDEFINED_ERROR:
			std::cerr << "Error: Something went wrong.\n";
			break;
		case netcode::UserRegistrationResponse_ErrorCode_OK:
			std::cout << "Request was OK, you are now registered.\n";
			break;
		case netcode::UserRegistrationResponse_ErrorCode_INVALID_PARAMETER:
			std::cerr << "Error: Invalid parameter\n";
			break;
		case netcode::UserRegistrationResponse_ErrorCode_EMPTY_FIELDS:
			std::cerr << "Error: Empty fields are not allowed.\n";
			break;
		case netcode::UserRegistrationResponse_ErrorCode_NOT_ALLOWED:
			std::cerr << "Error: You are not allowed to register.\n";
			break;
		default:
			std::cerr << "Error: Received an unknown error code\n";
			break;
	}

	return 0;
}