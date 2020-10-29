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
		std::vector<std::string> groupMemberMatrNumbers // Insert your group members matr.numbers (including yours)
				{
						"11819382"
				};
};

Settings settings;
StubPtr stub;

int groupRegistration();

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

	// call the remote procedure
	return groupRegistration();
}

int groupRegistration()
{
	// create the request
	netcode::GroupRegistrationRequest request;
	for (auto& member : settings.groupMemberMatrNumbers)
		request.add_matr_number(member);

	auto auth = new netcode::AuthPacket();
	auth->set_matr_number(settings.matrNr);
	auth->set_secret(settings.secret);
	request.set_allocated_auth(auth);

	// create required objects to use the rpc
	netcode::GroupRegistrationResponse response;
	grpc::ClientContext context; // NOTE: after a rpc uses the client context, it gets invalidated and cannot be reused

	// call the remote procedure from the stub
	grpc::Status status = stub->GroupRegistration(&context, request, &response);

	// check the response status
	if (!status.ok())
	{
		std::cerr << "Error: The request has been canceled by the server.\n";
		return 1;
	}

	switch (response.error_code())
	{
		case netcode::GroupRegistrationResponse_ErrorCode_UNDEFINED_ERROR:
			std::cerr << "Error: Undefined error.\n";
			break;
		case netcode::GroupRegistrationResponse_ErrorCode_OK:
			std::cout << "Registration successful.\n";
			break;
		case netcode::GroupRegistrationResponse_ErrorCode_UNKNOWN_USER:
			std::cerr << "Error: Unknown user.\n";
			break;
		case netcode::GroupRegistrationResponse_ErrorCode_TOO_MANY_GROUP_MEMBERS:
			std::cerr << "Error: Too many group members.\n";
			break;
		case netcode::GroupRegistrationResponse_ErrorCode_USER_ALREADY_REGISTERED:
			std::cerr << "Error: A user is already registered for a group.\n";
			break;
		case netcode::GroupRegistrationResponse_ErrorCode_AUTH_FAILED:
			std::cerr << "Error: Auth failed.\n";
			break;
		default:
			std::cerr << "Error: Unknown response error code.\n";
			return 2;
	}

	return 0;
}