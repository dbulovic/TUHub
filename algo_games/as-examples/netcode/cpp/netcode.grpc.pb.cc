// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: netcode.proto

#include "netcode.pb.h"
#include "netcode.grpc.pb.h"

#include <functional>
#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/channel_interface.h>
#include <grpcpp/impl/codegen/client_unary_call.h>
#include <grpcpp/impl/codegen/client_callback.h>
#include <grpcpp/impl/codegen/method_handler_impl.h>
#include <grpcpp/impl/codegen/rpc_service_method.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/sync_stream.h>
namespace netcode {

static const char* GameCom_method_names[] = {
  "/netcode.GameCom/NewMatch",
  "/netcode.GameCom/SubmitTurn",
  "/netcode.GameCom/GetGameState",
  "/netcode.GameCom/GetTimeout",
  "/netcode.GameCom/GetOpponentInfo",
  "/netcode.GameCom/AbortMatch",
  "/netcode.GameCom/UserRegistration",
  "/netcode.GameCom/GroupRegistration",
  "/netcode.GameCom/SetGroupPseudonym",
  "/netcode.GameCom/SetUserPseudonym",
  "/netcode.GameCom/GetUserToken",
};

std::unique_ptr< GameCom::Stub> GameCom::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< GameCom::Stub> stub(new GameCom::Stub(channel));
  return stub;
}

GameCom::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_NewMatch_(GameCom_method_names[0], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_SubmitTurn_(GameCom_method_names[1], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetGameState_(GameCom_method_names[2], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetTimeout_(GameCom_method_names[3], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetOpponentInfo_(GameCom_method_names[4], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_AbortMatch_(GameCom_method_names[5], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_UserRegistration_(GameCom_method_names[6], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GroupRegistration_(GameCom_method_names[7], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_SetGroupPseudonym_(GameCom_method_names[8], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_SetUserPseudonym_(GameCom_method_names[9], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetUserToken_(GameCom_method_names[10], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status GameCom::Stub::NewMatch(::grpc::ClientContext* context, const ::netcode::MatchRequest& request, ::netcode::MatchResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_NewMatch_, context, request, response);
}

void GameCom::Stub::experimental_async::NewMatch(::grpc::ClientContext* context, const ::netcode::MatchRequest* request, ::netcode::MatchResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_NewMatch_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::MatchResponse>* GameCom::Stub::AsyncNewMatchRaw(::grpc::ClientContext* context, const ::netcode::MatchRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::MatchResponse>::Create(channel_.get(), cq, rpcmethod_NewMatch_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::MatchResponse>* GameCom::Stub::PrepareAsyncNewMatchRaw(::grpc::ClientContext* context, const ::netcode::MatchRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::MatchResponse>::Create(channel_.get(), cq, rpcmethod_NewMatch_, context, request, false);
}

::grpc::Status GameCom::Stub::SubmitTurn(::grpc::ClientContext* context, const ::netcode::TurnRequest& request, ::netcode::TurnResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_SubmitTurn_, context, request, response);
}

void GameCom::Stub::experimental_async::SubmitTurn(::grpc::ClientContext* context, const ::netcode::TurnRequest* request, ::netcode::TurnResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_SubmitTurn_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::TurnResponse>* GameCom::Stub::AsyncSubmitTurnRaw(::grpc::ClientContext* context, const ::netcode::TurnRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::TurnResponse>::Create(channel_.get(), cq, rpcmethod_SubmitTurn_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::TurnResponse>* GameCom::Stub::PrepareAsyncSubmitTurnRaw(::grpc::ClientContext* context, const ::netcode::TurnRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::TurnResponse>::Create(channel_.get(), cq, rpcmethod_SubmitTurn_, context, request, false);
}

::grpc::Status GameCom::Stub::GetGameState(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::netcode::GameStateResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetGameState_, context, request, response);
}

void GameCom::Stub::experimental_async::GetGameState(::grpc::ClientContext* context, const ::netcode::MatchIDPacket* request, ::netcode::GameStateResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetGameState_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::GameStateResponse>* GameCom::Stub::AsyncGetGameStateRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GameStateResponse>::Create(channel_.get(), cq, rpcmethod_GetGameState_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::GameStateResponse>* GameCom::Stub::PrepareAsyncGetGameStateRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GameStateResponse>::Create(channel_.get(), cq, rpcmethod_GetGameState_, context, request, false);
}

::grpc::Status GameCom::Stub::GetTimeout(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::netcode::GetTimeoutResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetTimeout_, context, request, response);
}

void GameCom::Stub::experimental_async::GetTimeout(::grpc::ClientContext* context, const ::netcode::MatchIDPacket* request, ::netcode::GetTimeoutResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetTimeout_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::GetTimeoutResponse>* GameCom::Stub::AsyncGetTimeoutRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GetTimeoutResponse>::Create(channel_.get(), cq, rpcmethod_GetTimeout_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::GetTimeoutResponse>* GameCom::Stub::PrepareAsyncGetTimeoutRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GetTimeoutResponse>::Create(channel_.get(), cq, rpcmethod_GetTimeout_, context, request, false);
}

::grpc::Status GameCom::Stub::GetOpponentInfo(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::netcode::OpponentInfoResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetOpponentInfo_, context, request, response);
}

void GameCom::Stub::experimental_async::GetOpponentInfo(::grpc::ClientContext* context, const ::netcode::MatchIDPacket* request, ::netcode::OpponentInfoResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetOpponentInfo_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::OpponentInfoResponse>* GameCom::Stub::AsyncGetOpponentInfoRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::OpponentInfoResponse>::Create(channel_.get(), cq, rpcmethod_GetOpponentInfo_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::OpponentInfoResponse>* GameCom::Stub::PrepareAsyncGetOpponentInfoRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::OpponentInfoResponse>::Create(channel_.get(), cq, rpcmethod_GetOpponentInfo_, context, request, false);
}

::grpc::Status GameCom::Stub::AbortMatch(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::netcode::Nothing* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_AbortMatch_, context, request, response);
}

void GameCom::Stub::experimental_async::AbortMatch(::grpc::ClientContext* context, const ::netcode::MatchIDPacket* request, ::netcode::Nothing* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_AbortMatch_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::Nothing>* GameCom::Stub::AsyncAbortMatchRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::Nothing>::Create(channel_.get(), cq, rpcmethod_AbortMatch_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::Nothing>* GameCom::Stub::PrepareAsyncAbortMatchRaw(::grpc::ClientContext* context, const ::netcode::MatchIDPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::Nothing>::Create(channel_.get(), cq, rpcmethod_AbortMatch_, context, request, false);
}

::grpc::Status GameCom::Stub::UserRegistration(::grpc::ClientContext* context, const ::netcode::UserRegistrationRequest& request, ::netcode::UserRegistrationResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_UserRegistration_, context, request, response);
}

void GameCom::Stub::experimental_async::UserRegistration(::grpc::ClientContext* context, const ::netcode::UserRegistrationRequest* request, ::netcode::UserRegistrationResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_UserRegistration_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::UserRegistrationResponse>* GameCom::Stub::AsyncUserRegistrationRaw(::grpc::ClientContext* context, const ::netcode::UserRegistrationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::UserRegistrationResponse>::Create(channel_.get(), cq, rpcmethod_UserRegistration_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::UserRegistrationResponse>* GameCom::Stub::PrepareAsyncUserRegistrationRaw(::grpc::ClientContext* context, const ::netcode::UserRegistrationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::UserRegistrationResponse>::Create(channel_.get(), cq, rpcmethod_UserRegistration_, context, request, false);
}

::grpc::Status GameCom::Stub::GroupRegistration(::grpc::ClientContext* context, const ::netcode::GroupRegistrationRequest& request, ::netcode::GroupRegistrationResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GroupRegistration_, context, request, response);
}

void GameCom::Stub::experimental_async::GroupRegistration(::grpc::ClientContext* context, const ::netcode::GroupRegistrationRequest* request, ::netcode::GroupRegistrationResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GroupRegistration_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::GroupRegistrationResponse>* GameCom::Stub::AsyncGroupRegistrationRaw(::grpc::ClientContext* context, const ::netcode::GroupRegistrationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GroupRegistrationResponse>::Create(channel_.get(), cq, rpcmethod_GroupRegistration_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::GroupRegistrationResponse>* GameCom::Stub::PrepareAsyncGroupRegistrationRaw(::grpc::ClientContext* context, const ::netcode::GroupRegistrationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GroupRegistrationResponse>::Create(channel_.get(), cq, rpcmethod_GroupRegistration_, context, request, false);
}

::grpc::Status GameCom::Stub::SetGroupPseudonym(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::netcode::SetPseudonymResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_SetGroupPseudonym_, context, request, response);
}

void GameCom::Stub::experimental_async::SetGroupPseudonym(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest* request, ::netcode::SetPseudonymResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_SetGroupPseudonym_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::SetPseudonymResponse>* GameCom::Stub::AsyncSetGroupPseudonymRaw(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::SetPseudonymResponse>::Create(channel_.get(), cq, rpcmethod_SetGroupPseudonym_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::SetPseudonymResponse>* GameCom::Stub::PrepareAsyncSetGroupPseudonymRaw(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::SetPseudonymResponse>::Create(channel_.get(), cq, rpcmethod_SetGroupPseudonym_, context, request, false);
}

::grpc::Status GameCom::Stub::SetUserPseudonym(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::netcode::SetPseudonymResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_SetUserPseudonym_, context, request, response);
}

void GameCom::Stub::experimental_async::SetUserPseudonym(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest* request, ::netcode::SetPseudonymResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_SetUserPseudonym_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::SetPseudonymResponse>* GameCom::Stub::AsyncSetUserPseudonymRaw(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::SetPseudonymResponse>::Create(channel_.get(), cq, rpcmethod_SetUserPseudonym_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::SetPseudonymResponse>* GameCom::Stub::PrepareAsyncSetUserPseudonymRaw(::grpc::ClientContext* context, const ::netcode::SetPseudonymRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::SetPseudonymResponse>::Create(channel_.get(), cq, rpcmethod_SetUserPseudonym_, context, request, false);
}

::grpc::Status GameCom::Stub::GetUserToken(::grpc::ClientContext* context, const ::netcode::AuthPacket& request, ::netcode::GetUserTokenResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetUserToken_, context, request, response);
}

void GameCom::Stub::experimental_async::GetUserToken(::grpc::ClientContext* context, const ::netcode::AuthPacket* request, ::netcode::GetUserTokenResponse* response, std::function<void(::grpc::Status)> f) {
  return ::grpc::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetUserToken_, context, request, response, std::move(f));
}

::grpc::ClientAsyncResponseReader< ::netcode::GetUserTokenResponse>* GameCom::Stub::AsyncGetUserTokenRaw(::grpc::ClientContext* context, const ::netcode::AuthPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GetUserTokenResponse>::Create(channel_.get(), cq, rpcmethod_GetUserToken_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::netcode::GetUserTokenResponse>* GameCom::Stub::PrepareAsyncGetUserTokenRaw(::grpc::ClientContext* context, const ::netcode::AuthPacket& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderFactory< ::netcode::GetUserTokenResponse>::Create(channel_.get(), cq, rpcmethod_GetUserToken_, context, request, false);
}

GameCom::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::MatchRequest, ::netcode::MatchResponse>(
          std::mem_fn(&GameCom::Service::NewMatch), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::TurnRequest, ::netcode::TurnResponse>(
          std::mem_fn(&GameCom::Service::SubmitTurn), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[2],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::MatchIDPacket, ::netcode::GameStateResponse>(
          std::mem_fn(&GameCom::Service::GetGameState), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[3],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::MatchIDPacket, ::netcode::GetTimeoutResponse>(
          std::mem_fn(&GameCom::Service::GetTimeout), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[4],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::MatchIDPacket, ::netcode::OpponentInfoResponse>(
          std::mem_fn(&GameCom::Service::GetOpponentInfo), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[5],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::MatchIDPacket, ::netcode::Nothing>(
          std::mem_fn(&GameCom::Service::AbortMatch), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[6],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::UserRegistrationRequest, ::netcode::UserRegistrationResponse>(
          std::mem_fn(&GameCom::Service::UserRegistration), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[7],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::GroupRegistrationRequest, ::netcode::GroupRegistrationResponse>(
          std::mem_fn(&GameCom::Service::GroupRegistration), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[8],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::SetPseudonymRequest, ::netcode::SetPseudonymResponse>(
          std::mem_fn(&GameCom::Service::SetGroupPseudonym), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[9],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::SetPseudonymRequest, ::netcode::SetPseudonymResponse>(
          std::mem_fn(&GameCom::Service::SetUserPseudonym), this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GameCom_method_names[10],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GameCom::Service, ::netcode::AuthPacket, ::netcode::GetUserTokenResponse>(
          std::mem_fn(&GameCom::Service::GetUserToken), this)));
}

GameCom::Service::~Service() {
}

::grpc::Status GameCom::Service::NewMatch(::grpc::ServerContext* context, const ::netcode::MatchRequest* request, ::netcode::MatchResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::SubmitTurn(::grpc::ServerContext* context, const ::netcode::TurnRequest* request, ::netcode::TurnResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::GetGameState(::grpc::ServerContext* context, const ::netcode::MatchIDPacket* request, ::netcode::GameStateResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::GetTimeout(::grpc::ServerContext* context, const ::netcode::MatchIDPacket* request, ::netcode::GetTimeoutResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::GetOpponentInfo(::grpc::ServerContext* context, const ::netcode::MatchIDPacket* request, ::netcode::OpponentInfoResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::AbortMatch(::grpc::ServerContext* context, const ::netcode::MatchIDPacket* request, ::netcode::Nothing* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::UserRegistration(::grpc::ServerContext* context, const ::netcode::UserRegistrationRequest* request, ::netcode::UserRegistrationResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::GroupRegistration(::grpc::ServerContext* context, const ::netcode::GroupRegistrationRequest* request, ::netcode::GroupRegistrationResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::SetGroupPseudonym(::grpc::ServerContext* context, const ::netcode::SetPseudonymRequest* request, ::netcode::SetPseudonymResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::SetUserPseudonym(::grpc::ServerContext* context, const ::netcode::SetPseudonymRequest* request, ::netcode::SetPseudonymResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status GameCom::Service::GetUserToken(::grpc::ServerContext* context, const ::netcode::AuthPacket* request, ::netcode::GetUserTokenResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace netcode

